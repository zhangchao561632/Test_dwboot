"""读取数据文件"""
import yaml
import json
import pytest
import os

class Data(object):
    def __init__(self):
        pass

    def load_yaml(self, file_path):
        with open(file_path) as f:
            data = yaml.safe_load(f)
        return data

    def load_json(self, file_path):
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
        return data

    def case_data(self,file_path,case_data):
        return self.load_yaml(file_path).get(case_data)


# ww = Data().case_data(r'D:\TestTool\Python\Location\longteng17_1\longteng17\data\api_data.yaml','test_add_fuel_card_normal')
