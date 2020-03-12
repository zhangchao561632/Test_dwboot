import pytest_check as ck
import pytest

@pytest.mark.p0
@pytest.mark.app
@pytest.mark.skip
def test_login(login_page,driver):
    login_page.Login('18010181267','123456')
    ck.is_true(driver.find_elements_by_xpath('//*[@text="LQRWeChat"]'))

if __name__ == "__main__":
    pytest.main(["-s", r"D:\TestTool\Python\Location\longteng17_1\longteng17\test_cases\app_test\test_login.py"])

