import pytest
import pytest_check as ck

@pytest.mark.p1
@pytest.mark.api
def test_invest_fuel_card_normal(api, db, data):
    """正常充值加油卡"""
    request_data = data.get('test_invest_fuel_card_normal')
    card_number = request_data.get('json').get('CardInfo').get('cardNumber')
    #环境检查
    if not db.check_card(card_number):
        db.add_card(card_number)
    res_dict = api.request_all(request_data).json()
    print(f'响应数据{res_dict}')
    # 响应断言
    ck.equal(200, res_dict.get("code"))
    ck.equal("充值成功", res_dict.get("msg"))
    ck.is_true(res_dict.get('success'))

    # 环境清理
    db.del_card(card_number)

@pytest.mark.p1
@pytest.mark.api
def test_invest_fuel_card_norma2(api, db, data):
    """充值卡号不存在"""
    request_data = data.get('test_invest_fuel_card_norma2')
    res_dict = api.request_all(request_data).json()
    card_number = request_data.get('json').get('CardInfo').get('cardNumber')
    print(f'响应数据{res_dict}')
    #环境检查
    if db.check_card(card_number):
        db.del_card(card_number)
    # 响应断言
    ck.equal(5013, res_dict.get("code"))
    ck.equal("加油卡号不存在", res_dict.get("msg"))
    ck.is_false(res_dict.get('success'))

@pytest.mark.p1
@pytest.mark.api
def test_invest_fuel_card_norma3(api, db, data):
    """充值金额为空"""
    request_data = data.get('test_invest_fuel_card_norma3')
    card_number = request_data.get('json').get('CardInfo').get('cardNumber')
    #环境检查
    if not db.check_card(card_number):
        db.add_card(card_number)
    res_dict = api.request_all(request_data).json()
    print(f'响应数据{res_dict}')
    # 响应断言
    ck.equal(300, res_dict.get("code"))
    ck.equal("金额不能为空", res_dict.get("msg"))
    ck.is_false(res_dict.get('success'))

    #环境清理
    db.del_card(card_number)

@pytest.mark.p1
@pytest.mark.api
def test_invest_fuel_card_norma4(api, db, data):
    """充值金额为负数"""
    request_data = data.get('test_invest_fuel_card_norma4')
    card_number = request_data.get('json').get('CardInfo').get('cardNumber')
    #环境检查
    if not db.check_card(card_number):
        db.add_card(card_number)
    res_dict = api.request_all(request_data).json()
    print(f'响应数据{res_dict}')
    # 响应断言
    ck.equal(300, res_dict.get("code"))
    ck.equal("金额需为整数", res_dict.get("msg"))
    ck.is_false(res_dict.get('success'))

    #环境清理
    db.del_card(card_number)

def test_invest_fuel_card_norma5(api, db, data):
    """充值金额为字母、特殊字符"""
    request_data = data.get('test_invest_fuel_card_norma5')
    card_number = request_data.get('json').get('CardInfo').get('cardNumber')
    #环境检查
    if not db.check_card(card_number):
        db.add_card(card_number)
    res_dict = api.request_all(request_data).json()
    print(f'响应数据{res_dict}')
    # 响应断言
    ck.equal(300, res_dict.get("code"))
    ck.equal("金额需为整数", res_dict.get("msg"))
    ck.is_false(res_dict.get('success'))

    #环境清理
    db.del_card(card_number)

if __name__ == "__main__":
    pytest.main(["-s", r"D:\TestTool\Python\Location\longteng17_1\longteng17\test_cases\api_test\test_invest_fuel_card.py"])

