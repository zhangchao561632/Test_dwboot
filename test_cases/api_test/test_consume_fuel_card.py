import pytest
import pytest_check as ck

@pytest.mark.p1
@pytest.mark.api
def test_consume_fuel_card_normal(api,data):
    """正常消费加油卡"""
    request_data = data.get('test_consume_fuel_card_normal')
    res_dict = api.request_all(request_data).json()
    print(f'响应数据{res_dict}')
    # 响应断言
    ck.equal(200, res_dict.get("code"))
    ck.equal("消费成功!", res_dict.get("msg"))
    ck.is_true(res_dict.get('success'))

@pytest.mark.p1
@pytest.mark.api
def test_consume_fuel_card_norma2(api,data):
    """卡号和用户不对应"""
    request_data = data.get('test_consume_fuel_card_norma2')
    res_dict = api.request_all(request_data).json()
    print(f'响应数据{res_dict}')
    # 响应断言
    ck.equal(5013, res_dict.get("code"))
    ck.equal("根据用户ID没有查询到卡号!", res_dict.get("msg"))
    ck.is_false(res_dict.get('success'))

@pytest.mark.p1
@pytest.mark.api
def test_consume_fuel_card_norma3(api,data):
    """用户id（userId）为空"""
    request_data = data.get('test_consume_fuel_card_norma3')
    try:
        res_dict = api.request_all(request_data).json()
        print(f'响应数据{res_dict}')
        # 响应断言
        ck.equal(301, res_dict.get("code"))
        ck.almost_equal("参数类型错误com.alibaba.fastjson.JSONException", res_dict.get("msg"))
        ck.is_false(res_dict.get('success'))
    except:
        pass

@pytest.mark.p1
@pytest.mark.api
def test_consume_fuel_card_norma4(api,data):
    """消费金额为负数"""
    request_data = data.get('test_consume_fuel_card_norma4')
    res_dict = api.request_all(request_data).json()
    print(f'响应数据{res_dict}')
    # 响应断言
    ck.equal(200, res_dict.get("code"))
    ck.equal("消费成功!", res_dict.get("msg"))
    ck.is_true(res_dict.get('success'))

@pytest.mark.p1
@pytest.mark.api
def test_consume_fuel_card_norma5(api,data,db):
    """卡号余额不足"""
    request_data = data.get('test_consume_fuel_card_norma5')
    card_number = request_data.get('json').get('CardInfo').get('cardNumber')
    if db.reset_balance(card_number):
        res_dict = api.request_all(request_data).json()
        print(f'响应数据{res_dict}')
        ck.equal(200, res_dict.get("code"))
        ck.equal("对不起，您的余额不足，请充值!", res_dict.get("msg"))
        ck.is_false(res_dict.get('success'))

if __name__ == "__main__":
    pytest.main(["-s", r"D:\TestTool\Python\Location\longteng17_1\longteng17\test_cases\api_test\test_consume_fuel_card.py"])
