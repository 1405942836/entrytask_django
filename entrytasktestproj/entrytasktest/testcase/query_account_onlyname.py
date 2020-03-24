# -*- coding: utf-8 -*-
'''查询余额测试用例
'''
# 2020/03/24 QTAF自动生成

from entrytasktestproj.entrytasklib.testcase import EntrytaskTestCase
from entrytasktestproj.entrytasktest.testdata.query_account_data import query_account_ReqData
import requests

class QueryAccountTest_OnlyNameA(EntrytaskTestCase):
    '''查询余额测试用例
        登录态下
        请求参数中只有name：用户name只有数字
        价格默认空
        折扣默认空
    '''
    owner = "xuzhaozhou"
    timeout = 5
    priority = EntrytaskTestCase.EnumPriority.High
    status = EntrytaskTestCase.EnumStatus.Design

    def run_test(self):
        self.log_info("query account testcase")
        # self.assert_equal(True, True)
        # 构造json请求数据，用户name只有数字
        req_data = {'user_name': '001', 'product_price': '', 'product_discount': ''}
        resp_data = requests.get('http://127.0.0.1:8000/query_account_get_test', params=req_data)
        resp_data_json = resp_data.json()        # 转为json格式
        print(resp_data.url)                     # 打印响应URL
        print(resp_data_json)                    # 打印响应的json数据
        print(resp_data.status_code)             # 打印响应的状态码


class QueryAccountTest_OnlyNameB(EntrytaskTestCase):
    '''查询余额测试用例
        登录态下
        请求参数中只有name：用户name只有字母
        价格默认空
        折扣默认空
    '''
    owner = "xuzhaozhou"
    timeout = 5
    priority = EntrytaskTestCase.EnumPriority.High
    status = EntrytaskTestCase.EnumStatus.Design

    def run_test(self):
        self.log_info("query account testcase")
        # self.assert_equal(True, True)
        # 构造json请求数据，用户name只有字母
        req_data = {'user_name': 'xuzhao', 'product_price': '', 'product_discount': ''}
        resp_data = requests.get('http://127.0.0.1:8000/query_account_get_test', params=req_data)
        resp_data_json = resp_data.json()        # 转为json格式
        print(resp_data.url)                     # 打印响应URL
        print(resp_data_json)                    # 打印响应的json数据
        print(resp_data.status_code)             # 打印响应的状态码


class QueryAccountTest_OnlyNameC(EntrytaskTestCase):
    '''查询余额测试用例
        登录态下
        请求参数中只有name：用户name数字+字母组合
        价格默认空
        折扣默认空
    '''
    owner = "xuzhaozhou"
    timeout = 5
    priority = EntrytaskTestCase.EnumPriority.High
    status = EntrytaskTestCase.EnumStatus.Design

    def run_test(self):
        self.log_info("query account testcase")
        # self.assert_equal(True, True)
        # 构造json请求数据，用户name数字+字母组合
        req_data = {'user_name': 'xuzhao001', 'product_price': '', 'product_discount': ''}
        resp_data = requests.get('http://127.0.0.1:8000/query_account_get_test', params=req_data)
        resp_data_json = resp_data.json()        # 转为json格式
        print(resp_data.url)                     # 打印响应URL
        print(resp_data_json)                    # 打印响应的json数据
        print(resp_data.status_code)             # 打印响应的状态码


class QueryAccountTest_OnlyNameD(EntrytaskTestCase):
    '''查询余额测试用例
        登录态下
        请求参数中只有name：用户name数字+字母+符号组合
        价格默认空
        折扣默认空
    '''
    owner = "xuzhaozhou"
    timeout = 5
    priority = EntrytaskTestCase.EnumPriority.High
    status = EntrytaskTestCase.EnumStatus.Design

    def run_test(self):
        self.log_info("query account testcase")
        # self.assert_equal(True, True)
        # 构造json请求数据，用户name数字+字母+符号组合
        req_data = {'user_name': 'xuzhao_test001', 'product_price': '100', 'product_discount': '0.5'}
        resp_data = requests.get('http://127.0.0.1:8000/query_account_get_test', params=req_data)
        resp_data_json = resp_data.json()        # 转为json格式
        print(resp_data.url)                     # 打印响应URL
        print(resp_data_json)                    # 打印响应的json数据
        print(resp_data.status_code)             # 打印响应的状态码


if __name__ == '__main__':
    QueryAccountTest_OnlyNameA().debug_run()
    QueryAccountTest_OnlyNameB().debug_run()
    QueryAccountTest_OnlyNameC().debug_run()
    QueryAccountTest_OnlyNameD().debug_run()

