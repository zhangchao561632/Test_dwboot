import pytest
import pytest_check as ck

@pytest.mark.p0
@pytest.mark.api
def test_query_fuel_card_normal(api,data):
    '''正常查询加油卡'''
    request_data = data.get('test_query_fuel_card_normal')
    res_dict = api.request_all(request_data).json()
    print(f'响应数据{res_dict}')
    # 响应断言
    ck.equal(200, res_dict.get("code"))
    ck.equal("成功返回", res_dict.get("msg"))
    ck.is_true(res_dict.get('success'))

@pytest.mark.p1
@pytest.mark.api
def test_query_fuel_card_norma2(api,data):
    '''无查询信息'''
    request_data = data.get('test_query_fuel_card_norma2')
    res_dict = api.request_all(request_data).json()
    print(f'响应数据{res_dict}')
    # 响应断言
    ck.equal(400, res_dict.get("code"))
    ck.equal("无查询信息", res_dict.get("msg"))
    ck.is_false(res_dict.get('success'))

@pytest.mark.p2
@pytest.mark.api
def test_query_fuel_card_norma3(api,data):
    '''代码错误'''
    request_data3 = data.get('test_query_fuel_card_norma3')
    try:
        res_dict = api.request_all(request_data3).json()
        print(f'响应数据{res_dict}')
    except:
        pass

@pytest.mark.p2
@pytest.mark.api
def test_query_fuel_card_norma4(api,data):
    '''代码错误'''
    try:
        request_data4 = data.get('test_query_fuel_card_norma4')
        res_dict = api.request_all(request_data4).json()
        print(f'响应数据{res_dict}')
    except:
        pass

@pytest.mark.p2
@pytest.mark.api
def test_query_fuel_card_norma5(api,data):
    '''代码错误'''
    try:
        request_data5 = data.get('test_query_fuel_card_norma5')
        res_dict = api.request_all(request_data5).json()
        print(f'响应数据{res_dict}')
    except:
        pass


if __name__ == "__main__":
    pytest.main(["-s", r"D:\TestTool\Python\Location\longteng17_1\longteng17\test_cases\api_test\test_query_fuel_card.py"])
