# -*- coding: utf-8 -*-
'''查询余额测试用例
'''
# 2020/03/24 QTAF自动生成

from entrytasktestproj.entrytasklib.testcase import EntrytaskTestCase
from entrytasktestproj.entrytasktest.testdata.query_account_data import query_account_ReqData
import requests

class QueryAccountTest_NotNameA(EntrytaskTestCase):
    '''查询余额测试用例
        非登录态下
        name为空
        价格默认100
        折扣默认0.5
    '''
    owner = "xuzhaozhou"
    timeout = 5
    priority = EntrytaskTestCase.EnumPriority.High
    status = EntrytaskTestCase.EnumStatus.Design

    def run_test(self):
        self.log_info("query account testcase")
        # self.assert_equal(True, True)
        # 构造json请求数据，价格为空，折扣不为空
        req_data = {'user_name': 'xuzhao_test001', 'product_price': '', 'product_discount': '0.5'}
        resp_data = requests.get('http://127.0.0.1:8000/query_account_get_test', params=req_data)
        resp_data_json = resp_data.json()        # 转为json格式
        print(resp_data.url)                     # 打印响应URL
        print(resp_data_json)                    # 打印响应的json数据
        print(resp_data.status_code)             # 打印响应的状态码


class QueryAccountTest_NotNameB(EntrytaskTestCase):
    '''查询余额测试用例
        非登录态下
        name为空
        价格默认100
        折扣默认0.5
    '''
    owner = "xuzhaozhou"
    timeout = 5
    priority = EntrytaskTestCase.EnumPriority.High
    status = EntrytaskTestCase.EnumStatus.Design

    def run_test(self):
        self.log_info("query account testcase")
        # self.assert_equal(True, True)
        # 构造json请求数据，价格price不为空，折扣discount为空
        req_data = {'user_name': 'xuzhao_test001', 'product_price': '100', 'product_discount': ''}
        resp_data = requests.get('http://127.0.0.1:8000/query_account_get_test', params=req_data)
        resp_data_json = resp_data.json()        # 转为json格式
        print(resp_data.url)                     # 打印响应URL
        print(resp_data_json)                    # 打印响应的json数据
        print(resp_data.status_code)             # 打印响应的状态码


class QueryAccountTest_NotNameC(EntrytaskTestCase):
    '''查询余额测试用例
        非登录态下
        name为空
        价格默认100
        折扣默认0.5
    '''
    owner = "xuzhaozhou"
    timeout = 5
    priority = EntrytaskTestCase.EnumPriority.High
    status = EntrytaskTestCase.EnumStatus.Design

    def run_test(self):
        self.log_info("query account testcase")
        # self.assert_equal(True, True)
        # 构造json请求数据，价格，折扣均为空
        req_data = {'user_name': 'xuzhao_test001', 'product_price': '', 'product_discount': ''}
        resp_data = requests.get('http://127.0.0.1:8000/query_account_get_test', params=req_data)
        resp_data_json = resp_data.json()        # 转为json格式
        print(resp_data.url)                     # 打印响应URL
        print(resp_data_json)                    # 打印响应的json数据
        print(resp_data.status_code)             # 打印响应的状态码


class QueryAccountTest_NotNameD(EntrytaskTestCase):
    '''查询余额测试用例
        非登录态下
        name为空
        价格默认100
        折扣默认0.5
    '''
    owner = "xuzhaozhou"
    timeout = 5
    priority = EntrytaskTestCase.EnumPriority.High
    status = EntrytaskTestCase.EnumStatus.Design

    def run_test(self):
        self.log_info("query account testcase")
        # self.assert_equal(True, True)
        # 构造json请求数据，价格，折扣均不为空
        req_data = {'user_name': 'xuzhao_test001', 'product_price': '100', 'product_discount': '0.5'}
        resp_data = requests.get('http://127.0.0.1:8000/query_account_get_test', params=req_data)
        resp_data_json = resp_data.json()        # 转为json格式
        print(resp_data.url)                     # 打印响应URL
        print(resp_data_json)                    # 打印响应的json数据
        print(resp_data.status_code)             # 打印响应的状态码


if __name__ == '__main__':
    QueryAccountTest_NotNameA().debug_run()
    QueryAccountTest_NotNameB().debug_run()
    QueryAccountTest_NotNameC().debug_run()
    QueryAccountTest_NotNameD().debug_run()

