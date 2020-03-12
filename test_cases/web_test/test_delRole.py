import pytest,allure
import pytest_check as ck

@allure.feature("登录模块")
class TestLogin(object):
    #@pytest.mark.skip
    @pytest.mark.p0
    @pytest.mark.web
    @allure.story("测试正常登录")
    def test_login(self,Login_page,selenium):
        user_name = 'root'
        passwd = '123456'
        result_loc = ('xpath','//li[@class="hidden-mobile"]/header-user/div')
        Login_page.login(user_name,passwd)
        user_text = selenium.find_element(*result_loc).text
        ck.equal(user_name, user_text)

@allure.feature("角色管理模块")
class TestRole():
    #@pytest.mark.skip
    @pytest.mark.p0
    @pytest.mark.web
    @allure.story("测试添加角色")
    def test_add_role(self,add_role_page,db,selenium):
        roleName = '测试角色'
        roleMark = '测试角色'
        if db.check_role(roleName): #环境检查
            db.del_role(roleName)
        add_role_page.add_Role(roleName,roleMark)
        lens =len(selenium.find_elements('xpath',f'//span[text()="{roleName}"]'))
        ck.greater(lens,0) #断言
        db.del_role(roleName) # 环境清理

if __name__ == "__main__":
    pytest.main(["-s", r"D:\TestTool\Pycham-workdir\Test_dwboot\test_dwboot\test_cases\web_test\test_delRole.py"])


