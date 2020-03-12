from selenium import webdriver
import logging
import time

class LoginPage():
    user_inp_loc =('xpath','//input[@formcontrolname="userName"]')
    password_inp_loc = ('xpath','//input[@formcontrolname="password"]')
    login_btn_loc = ('xpath','//button[@type="submit"]')
    def __init__(self,driver):
        self.driver = driver
        #driver = webdriver.Chrome()
        # driver.switch_to_default_content()
        # driver.maximize_window()

    def send_user_inp_loc(self,user):
        self.driver.find_element(*self.user_inp_loc).clear()
        self.driver.find_element(*self.user_inp_loc).send_keys(user)
        logging.info('输入登录用户名')

    def send_password_inp_loc(self,password):
        self.driver.find_element(*self.password_inp_loc).clear()
        self.driver.find_element(*self.password_inp_loc).send_keys(password)
        logging.info('输入登录密码')

    def click_login_btn_loc(self):
        time.sleep(2)
        self.driver.find_element(*self.login_btn_loc).click()
        logging.info('点击登录')

    def login(self,user,password):
        self.send_user_inp_loc(user)
        self.send_password_inp_loc(password)
        self.click_login_btn_loc()

class MenuPage():
    def __init__(self,driver):
        self.driver = driver

    def main_menu_sub_menu(self,main_menu,sub_menu):
        main_menu_loc = ('xpath', f'//span[text()="{main_menu}"]')
        sub_menu_loc = ('xpath', f'//a[contains(text(),"{sub_menu}")]')
        self.driver.find_element(*main_menu_loc).click()
        logging.info('点击主菜单')
        self.driver.find_element(*sub_menu_loc).click()
        logging.info('点击二级菜单')

class Role_management():
    add_Roles_bnt_loc = ('xpath','//div[@class="ant-col ant-col-16"]/button[1]')
    roleName_inp_loc = ('xpath','//input[@formcontrolname="roleName"]')
    roleMark_inp_loc = ('xpath','//input[@formcontrolname="remark"]')
    subRole_bnt_loc = ('xpath','//button[@class="login-form-button ant-btn ant-btn-primary"]')
    def __init__(self, driver):
        self.driver = driver

    def add_Roles_bnt(self):
        self.driver.find_element(*self.add_Roles_bnt_loc).click()
        logging.info('点击添加角色按钮')

    def role_Name(self,roleName):
        self.driver.find_element(*self.roleName_inp_loc).send_keys(roleName)
        logging.info('输入角色名称')

    def role_Mark(self,roleMark):
        self.driver.find_element(*self.roleMark_inp_loc).send_keys(roleMark)
        logging.info('输入备注')

    def subRole(self):
        self.driver.find_element(*self.subRole_bnt_loc).click()
        logging.info('点击提交按钮')

    def add_Role(self,roleName,roleMark):
        self.add_Roles_bnt()
        self.role_Name(roleName)
        self.role_Mark(roleMark)
        self.subRole()