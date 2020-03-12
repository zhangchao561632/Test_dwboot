import pytest
from appium import webdriver
from app_pages import LoginPage

@pytest.fixture(scope='session')
def driver():
    caps = {
        "platformName": "Android",
        "platformVersion": "5.1.1",
        "deviceName": "127.0.0.1:62001",
        "appPackage": "com.lqr.wechat",
        "appActivity": "com.lqr.wechat.ui.activity.SplashActivity",
        "unicodeKeyboard": True,
        "resetKeyboard": True,
        "autoLaunch": False
      }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
    driver.implicitly_wait(10)
    return driver

@pytest.fixture(scope='function', autouse=True)
def boot_close_app(driver):
    driver.launch_app()
    yield driver
    driver.quit()

@pytest.fixture
def login_page(boot_close_app):
    return LoginPage(boot_close_app)
