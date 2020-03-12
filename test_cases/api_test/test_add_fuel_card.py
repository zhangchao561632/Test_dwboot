import pytest
import pytest_check as ck

@pytest.mark.p1
@pytest.mark.api
def test_add_fuel_card_normal(api, db, data):
    #正常添加加油卡
    request_data =data.get('test_add_fuel_card_normal')
    card_number = request_data.get('json').get('CardInfo').get('cardNumber')
    #环境检查
    if db.check_card(card_number):
        db.del_card(card_number)
    # 响应断言
    res_dict = api.request_all(request_data).json()
    print(f'响应数据{res_dict}')
    ck.equal(200, res_dict.get("code"))
    ck.equal("添加卡成功", res_dict.get("msg"))
    ck.is_false(res_dict.get('success'))
    # 数据库断言
    ck.is_true(db.check_card(card_number))
    # 环境清理
    db.del_card(card_number)

@pytest.mark.p1
@pytest.mark.api
def test_add_fuel_card_norma2(api, db, data):
    """添加已存在的加油卡"""
    request_data = data.get('test_add_fuel_card_norma2')
    card_number = request_data.get('json').get('CardInfo').get('cardNumber')
    #环境检查
    if not db.check_card(card_number):
        db.add_card(card_number)
    res_dict = api.request_all(request_data).json()
    print(f'响应数据{res_dict}')
    # 响应断言
    ck.equal(5000, res_dict.get("code"))
    ck.equal("该卡已添加", res_dict.get("msg"))
    ck.is_false(res_dict.get('success'))
    # 数据库断言
    ck.is_true(db.check_card(card_number))
    # 环境清理
    db.del_card(card_number)

@pytest.mark.p2
@pytest.mark.api
def test_add_fuel_card_norma3(api,data):
    """第三方机构无权限访问该接口"""
    request_data = data.get('test_add_fuel_card_norma3')
    res_dict = api.request_all(request_data).json()
    print(f'响应数据{res_dict}')
    # 响应断言
    ck.equal(100, res_dict.get("code"))
    ck.equal("对不起,您的第三方机构无权限访问该接口", res_dict.get("msg"))
    ck.is_false(res_dict.get('success'))

@pytest.mark.p2
@pytest.mark.api
def test_add_fuel_card_norma4(api,data):
    """第三方平台ID不能为空"""
    request_data = data.get('test_add_fuel_card_norma4')
    res_dict = api.request_all(request_data).json()
    print(f'响应数据{res_dict}')
    # 响应断言
    ck.equal(301, res_dict.get("code"))
    ck.equal("第三方平台ID不能为空!", res_dict.get("msg"))
    ck.is_false(res_dict.get('success'))


if __name__ == "__main__":
    pytest.main(["-s", r"D:\TestTool\Pycham-workdir\Test_dwboot\test_dwboot\test_cases\api_test\test_add_fuel_card.py"])

# if __name__ == '__main__':
#     pytest.main(['test_add_fuel_card.py::', '-s'])