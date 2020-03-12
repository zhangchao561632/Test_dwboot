import os
import pytest
from utils.data import Data
from utils.db import FuelCardDB,basedir_path
from utils.api import Api

@pytest.fixture(scope='session')
def data(request):
    #basedir = request.config.rootdir
    try:
        data_file_path = os.path.join(basedir_path(), 'data', 'api_data.yaml')
        data = Data().load_yaml(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return data

@pytest.fixture
def case_data(request, data):
    case_name = request.function.__name__
    print(case_name)
    return data.get(case_name)

@pytest.fixture(scope='session')
def db():
    try:
        db = FuelCardDB()
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        yield db
        db.close()

@pytest.fixture(scope='session')
def api():
    api = Api()
    return api

@pytest.fixture
def case_data(request):
    case_data=request.param #从request中取传递过来的参数
    print(case_data)
    return case_data

@pytest.fixture(scope='session', autouse=True)
def setup_teardown_sql(db):
    setup_sql = os.path.join(basedir_path(), 'data', 'setup.sql')
    teardown_sql = os.path.join(basedir_path(), 'data', 'teardown.sql')
    db.execute_file(setup_sql)
    yield
    db.execute_file(teardown_sql)