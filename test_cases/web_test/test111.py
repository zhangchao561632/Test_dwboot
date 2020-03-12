# from selenium import webdriver
# import time
# driver = webdriver.Chrome()
# driver.get('http://192.168.1.22:20004/#/passport/login')
# time.sleep(2)
# driver.find_element_by_xpath('//button[@type="submit"]').click()
# time.sleep(3)
# driver.find_element_by_xpath('//span[text()="系统管理"]').click()
# time.sleep(3)
# driver.find_element_by_xpath('//a[contains(text(),"角色管理")]').click()
# time.sleep(3)
# driver.find_element_by_xpath('//div[@class="ant-col ant-col-16"]/button[1]').click()
# time.sleep(3)
# driver.find_element_by_xpath('//input[@formcontrolname="roleName"]').send_keys("322")
# time.sleep(3)
# driver.find_element_by_xpath('//input[@formcontrolname="remark"]').send_keys("322")
# time.sleep(3)
# driver.find_element_by_xpath('//button[@class="login-form-button ant-btn ant-btn-primary"]').click()
# time.sleep(3)
# driver.quit()
#




# sql ='select * from SYS_ROLE t'
# import cx_Oracle
# DB_URI='boot2/boot2@192.168.1.21:1521/orcl'
#
# conn=cx_Oracle.connect(DB_URI)
# cursor=conn.cursor()
# cursor.execute (sql)
# row=cursor.fetchone()
# print(row[3])
# cursor.close()

# tns=cx_Oracle.makedsn('192.168.1.21',1521,'orcl')
# conn=cx_Oracle.connect('DCADMIN','DCADMIN',tns)
# cursor=conn.cursor()
# cursor.execute (sql)
# row=cursor.fetchone()
# print(row[2])
# conn.close()













