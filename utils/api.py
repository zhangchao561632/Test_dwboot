"""请求方法的封装"""
import requests

TIMEOUT = 30

class Api(object):
    def __init__(self):
        self.session = requests.session()
        self.base_url = 'http://115.28.108.130:8080'

    def request(self, method, url, **kwargs):
        url = self.base_url + url if self.base_url else url
        kwargs['timeout'] = kwargs.get('timeout', TIMEOUT)
        print(f"请求数据: GET {url} {kwargs}")
        res = self.session.request(method, url, **kwargs)
        print(f"响应数据: {res.text}")
        return res

    def get(self, url, **kwargs):
        return self.request('get', url, **kwargs)

    def post(self, url, **kwargs):
        return self.request('post', url, **kwargs)

    def request_all(self,request_data):
        res = requests.request(**request_data)
        return res