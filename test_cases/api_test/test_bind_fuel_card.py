import pytest
import pytest_check as ck

@pytest.mark.p1
@pytest.mark.api
def test_bind_fuel_card_normal(api,data,db):
    """绑定不存在的加油卡"""
    request_data = data.get('test_bind_fuel_card_normal')
    card_number = request_data.get('json').get('CardInfo').get('cardNumber')
    #环境检查
    if db.check_card(card_number):
        db.del_card(card_number)
    res_dict = api.request_all(request_data).json()
    print(f'响应数据{res_dict}')
    # 响应断言
    ck.equal(5013, res_dict.get("code"))
    ck.equal("加油卡号不存在", res_dict.get("msg"))
    ck.is_false(res_dict.get('success'))

@pytest.mark.p1
@pytest.mark.api
def test_bind_fuel_card_norma2(api,data,db):
    """正常绑定加油卡"""
    request_data = data.get('test_bind_fuel_card_normal')
    card_number = request_data.get('json').get('CardInfo').get('cardNumber')
    #环境检查
    if not db.check_card(card_number):
        db.add_card(card_number)
    else:
        db.reset_card(card_number)
    res_dict = api.request_all(request_data).json()
    print(f'响应数据{res_dict}')
    # 响应断言
    ck.equal(5010, res_dict.get("code"))
    ck.equal("绑定成功", res_dict.get("msg"))
    ck.is_true(res_dict.get('success'))
    #环境清理
    db.del_card(card_number)

@pytest.mark.p2
@pytest.mark.api
def test_bind_fuel_card_norma3(api,data,db):
    """绑定已经绑定的加油卡"""
    request_data = data.get('test_bind_fuel_card_norma3')
    card_number = request_data.get('json').get('CardInfo').get('cardNumber')
    userName = request_data.get('json').get('CardUser').get('userName')
    #环境检查
    if db.bind_card(card_number,userName):
        res_dict = api.request_all(request_data).json()
        print(f'响应数据{res_dict}')
        # 响应断言
        ck.equal(5041, res_dict.get("code"))
        ck.equal("卡已经被绑定,无法绑定", res_dict.get("msg"))
        ck.is_false(res_dict.get('success'))

    #环境清理
    db.del_card(card_number)

@pytest.mark.p2
@pytest.mark.api
def test_bind_fuel_card_norma4(api,data):
    """证件号为空"""
    request_data = data.get('test_bind_fuel_card_norma4')
    res_dict = api.request_all(request_data).json()
    print(f'响应数据{res_dict}')
    # 响应断言
    ck.equal(301, res_dict.get("code"))
    ck.equal("证件号不能为空!", res_dict.get("msg"))
    ck.is_false(res_dict.get('success'))

@pytest.mark.p2
@pytest.mark.api
def test_bind_fuel_card_norma5(api,data):
    """用户名称（username）为空!"""
    request_data = data.get('test_bind_fuel_card_norma5')
    res_dict = api.request_all(request_data).json()
    print(f'响应数据{res_dict}')
    # 响应断言
    ck.equal(301, res_dict.get("code"))
    ck.equal("用户名称不能为空!", res_dict.get("msg"))
    ck.is_false(res_dict.get('success'))

@pytest.mark.p2
@pytest.mark.api
def test_bind_fuel_card_norma6(api,data):
    """业务ID为空!"""
    request_data = data.get('test_bind_fuel_card_norma6')
    res_dict = api.request_all(request_data).json()
    print(f'响应数据{res_dict}')
    # 响应断言
    ck.equal(301, res_dict.get("code"))
    ck.equal("业务ID不能为空!", res_dict.get("msg"))
    ck.is_false(res_dict.get('success'))

@pytest.mark.p2
@pytest.mark.api
def test_bind_fuel_card_norma7(api,data):
    """证件类型为空"""
    request_data = data.get('test_bind_fuel_card_norma7')
    res_dict = api.request_all(request_data).json()
    print(f'响应数据{res_dict}')
    # 响应断言
    ck.equal(5031, res_dict.get("code"))
    ck.equal("证件类型不能为空!", res_dict.get("msg"))
    ck.is_false(res_dict.get('success'))

@pytest.mark.p2
@pytest.mark.api
def test_bind_fuel_card_norma8(api,data):
    """业务ID无效"""
    request_data = data.get('test_bind_fuel_card_norma8')
    res_dict = api.request_all(request_data).json()
    print(f'响应数据{res_dict}')
    # 响应断言
    ck.equal(199, res_dict.get("code"))
    ck.equal("业务ID无效", res_dict.get("msg"))
    ck.is_false(res_dict.get('success'))

@pytest.mark.p1
@pytest.mark.api
def test_bind_fuel_card_norma9(api,data,db):
    """每个用户只能绑定两张卡"""
    request_data = data.get('test_bind_fuel_card_norma9')
    #环境检查
    card_number1 = '8448646'
    card_number2 = '98893'
    card_name = 'zhangchao1'
    bind_card =[(card_number1,card_name),(card_number2,card_name)]
    card_number = request_data.get('json').get('CardInfo').get('cardNumber')
    for bind_data in bind_card:
        db.bind_card(*bind_data)

    if not db.check_card(card_number):
        db.add_card(card_number)
    else:
        db.reset_card(card_number)
    res_dict = api.request_all(request_data).json()
    print(f'响应数据{res_dict}')

    # 响应断言
    ck.equal(5014, res_dict.get("code"))
    ck.equal("每个用户只能绑定两张卡", res_dict.get("msg"))
    ck.is_false(res_dict.get('success'))

    #环境清理
    db.del_card(card_number1)
    db.del_card(card_number1)

if __name__ == "__main__":
    pytest.main(["-s", r"D:\TestTool\Python\Location\longteng17_1\longteng17\test_cases\api_test\test_bind_fuel_card.py"])
