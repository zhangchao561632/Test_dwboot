import pytest
from pages import LoginPage,MenuPage,Role_management
from utils.db import AddRoleDB
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@pytest.fixture(scope='session')
def selenium(chrome_options):
    docker = 0
    container_url = 'http://192.168.1.200:4444/wd/hub' #docker容器远程地址
    if docker==0:
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.implicitly_wait(10) #全局等待时间
        yield driver
        driver.quit()
    else:
        driver = webdriver.Remote(command_executor=container_url,
                                  desired_capabilities=DesiredCapabilities.CHROME)
        driver.implicitly_wait(10)  # 全局等待时间
        yield driver
        driver.quit()

@pytest.fixture(scope='session')
def chrome_options():
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')   #最大化启动浏览器
    # chrome_options.add_argument('--headless')
    return chrome_options

@pytest.fixture
def Login_page(selenium):
    selenium.get('http://192.168.1.22:20004/#/passport/login')
    return LoginPage(selenium)

@pytest.fixture
def menu_page(Login_page,selenium):
    Login_page.login('root','123456')
    return MenuPage(selenium)

@pytest.fixture
def add_role_page(menu_page,selenium):
    menu_page.main_menu_sub_menu('系统管理','角色管理')
    return  Role_management(selenium)

@pytest.fixture(scope='session')
def db():
    try:
        db = AddRoleDB()
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        yield db
        db.close()