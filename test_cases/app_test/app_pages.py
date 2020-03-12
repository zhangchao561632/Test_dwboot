
class LoginPage():
    Login__loc = ('id','com.lqr.wechat:id/btnLogin')
    Phone_inp_loc = ('id','com.lqr.wechat:id/etPhone')
    Password_inp_loc = ('id','com.lqr.wechat:id/etPwd')
    Login_buttn_loc = ('id','com.lqr.wechat:id/btnLogin')
    def __init__(self,driver):
        self.driver = driver

    def LoginButtn(self):
        self.driver.find_element(*self.Login__loc).click()

    def PhoneNumber(self,phone):
        self.driver.find_element(*self.Phone_inp_loc).send_keys(phone)

    def Password(self,password):
        self.driver.find_element(*self.Password_inp_loc).send_keys(password)

    def Click_loginButtn(self):
        self.driver.find_element(*self.Login_buttn_loc).click()

    def Login(self,phone,password):
        self.LoginButtn()
        self.PhoneNumber(phone)
        self.Password(password)
        self.Click_loginButtn()
