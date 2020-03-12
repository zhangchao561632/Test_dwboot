"""
数据库操作, 暂时只支持MySQL,
需要再环境变量中配置DB_URI=mysql://root:password@localhost:3306/test
"""
import os
import re
import cx_Oracle

def parse_db_uri(db_uri):
    """从db_uri中解析出数据host,port,db,user,password等信息，返回字典格式的数据库配置"""
    try:
        db_type, user, password, host, port, db = re.split(r'://|:|@|/', db_uri)
    except ValueError:
        raise ValueError(f'db_uri: {db_uri} - 格式不正确，应为完整的 mysql://root:password@localhost:3306/test 形式')
    if 'mysql' not in db_type:
        raise TypeError('暂时只支持mysql数据库')

    db_conf = dict(host=host, port=int(port), db=db, user=user, password=password)
    return db_conf

def basedir_path():
    BASEDIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    return BASEDIR

class DB(object):
    def __init__(self):
        ORACLE_URI = os.getenv('ORACLE_URI')
        if ORACLE_URI is None:
            raise ValueError('ORACLE_URI环境变量未配置, 格式为ORACLE_URI=用户名/密码@192.168.1.21:1521/orcl')
        self.conn = cx_Oracle.connect(ORACLE_URI)
        self.cur = self.conn.cursor()

    def query(self, sql):
        """执行sql"""
        print(f'查询sql: {sql}')
        self.cur.execute(sql)
        result = self.cur.fetchall()
        print(f"查询数据: {result}")
        return result

    def change_db(self, sql):
        print(f'执行sql: {sql}')
        self.cur.execute(sql)

    def execute_file(self, file_path):
        with open(file_path) as f:
            sqls = f.readlines()
        return [self.change_db(sql) for sql in sqls]

    def close(self):
        self.cur.close()
        self.conn.commit()

class AddRoleDB(DB):
    def del_role(self, role_name):
        sql = f"delete from SYS_ROLE t where t.role_name='{role_name}'"
        self.change_db(sql)

    def check_role(self, role_name):
        sql = f"select t.role_name from SYS_ROLE t where t.role_name='{role_name}'"
        res = self.query(sql)
        return True if res else False

class FuelCardDB(DB):
    def del_card(self, card_number):
        sql = f'DELETE FROM cardinfo WHERE cardNumber="{card_number}"'
        self.change_db(sql)

    def check_card(self, card_number):
        sql = f'SELECT id FROM cardinfo WHERE cardNumber="{card_number}"'
        res = self.query(sql)
        return True if res else False

    def add_card(self, card_number):
        sql = f'INSERT INTO cardinfo (cardNumber) VALUES ({card_number})'
        self.change_db(sql)

    def check_card_bind(self, card_number):
        sql = f'SELECT userid FROM cardinfo WHERE cardNumber="{card_number}"'
        res = self.query(sql)
        for res1 in res:
            if str(res1['userid'])=='None':
                return True

    def add_card_if_not_exist(self, card_number):
        if not self.check_card(card_number):
            sql = f'INSERT INTO cardinfo (`cardNumber`) VALUES ("{card_number}")'
            self.change_db(sql)
            return True
        return False

    def reset_card(self, card_number):
        sql = f'UPDATE cardinfo SET cardstatus=0, userId=null WHERE cardNumber="{card_number}";'
        self.change_db(sql)

    def bind_card(self, card_number, user_name):
        self.add_card_if_not_exist(card_number)
        sql = f'UPDATE cardinfo SET cardstatus=5010, userId=(SELECT userId FROM carduser WHERE userName="{user_name}" LIMIT 1) WHERE cardNumber="{card_number}";'
        self.change_db(sql)
        return True

    def get_user_id(self, user_name):
        sql = f'SELECT userId FROM carduser WHERE userName="{user_name}"'
        result, = self.query(sql) or [{}]
        user_id = result.get('userId', None)
        return user_id

    def reset_balance(self,card_number):
        sql = f'UPDATE cardinfo SET cardBalance="0" WHERE cardNumber="{card_number}";'
        self.change_db(sql)
        return True