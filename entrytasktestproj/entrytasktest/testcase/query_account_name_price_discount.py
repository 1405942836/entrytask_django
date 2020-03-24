# -*- coding: utf-8 -*-
'''查询余额测试用例
'''
# 2020/03/24 QTAF自动生成

from entrytasktestproj.entrytasklib.testcase import EntrytaskTestCase
from entrytasktestproj.entrytasktest.testdata.query_account_data import query_account_ReqData
import requests

class QueryAccountTest_NamePriceDiscountA(EntrytaskTestCase):
    '''查询余额测试用例
        登录态下
        请求参数中带name+price：用户name默认字母+数字+字符
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
        # 构造json请求数据，价格price*折扣discount小于用户余额account
        req_data = {'user_name': 'xuzhao_test001', 'product_price': '100', 'product_discount': '0.5'}
        resp_data = requests.get('http://127.0.0.1:8000/query_account_get_test', params=req_data)
        resp_data_json = resp_data.json()        # 转为json格式
        print(resp_data.url)                     # 打印响应URL
        print(resp_data_json)                    # 打印响应的json数据
        print(resp_data.status_code)             # 打印响应的状态码


class QueryAccountTest_NamePriceDiscountB(EntrytaskTestCase):
    '''查询余额测试用例
        登录态下
        请求参数中带name+price：用户name默认字母+数字+字符
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
        # 构造json请求数据，价格price*折扣discount等于用户余额account
        req_data = {'user_name': 'xuzhao_test001', 'product_price': '200', 'product_discount': '0.5'}
        resp_data = requests.get('http://127.0.0.1:8000/query_account_get_test', params=req_data)
        resp_data_json = resp_data.json()        # 转为json格式
        print(resp_data.url)                     # 打印响应URL
        print(resp_data_json)                    # 打印响应的json数据
        print(resp_data.status_code)             # 打印响应的状态码


class QueryAccountTest_NamePriceDiscountC(EntrytaskTestCase):
    '''查询余额测试用例
        登录态下
        请求参数中带name+price：用户name默认字母+数字+字符
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
        # 构造json请求数据，价格price*折扣discount大于用户余额account
        req_data = {'user_name': 'xuzhao_test001', 'product_price': '300', 'product_discount': '0.5'}
        resp_data = requests.get('http://127.0.0.1:8000/query_account_get_test', params=req_data)
        resp_data_json = resp_data.json()        # 转为json格式
        print(resp_data.url)                     # 打印响应URL
        print(resp_data_json)                    # 打印响应的json数据
        print(resp_data.status_code)             # 打印响应的状态码


class QueryAccountTest_NamePriceDiscountD(EntrytaskTestCase):
    '''查询余额测试用例
        登录态下
        请求参数中带name+price：用户name默认字母+数字+字符
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
        # 构造json请求数据，价格price为0，折扣discount不为0
        req_data = {'user_name': 'xuzhao_test001', 'product_price': '0', 'product_discount': '0.5'}
        resp_data = requests.get('http://127.0.0.1:8000/query_account_get_test', params=req_data)
        resp_data_json = resp_data.json()        # 转为json格式
        print(resp_data.url)                     # 打印响应URL
        print(resp_data_json)                    # 打印响应的json数据
        print(resp_data.status_code)             # 打印响应的状态码


class QueryAccountTest_NamePriceDiscountE(EntrytaskTestCase):
    '''查询余额测试用例
        登录态下
        请求参数中带name+price：用户name默认字母+数字+字符
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
        # 构造json请求数据，价格price不为0，折扣discount为0
        req_data = {'user_name': 'xuzhao_test001', 'product_price': '100', 'product_discount': '0'}
        resp_data = requests.get('http://127.0.0.1:8000/query_account_get_test', params=req_data)
        resp_data_json = resp_data.json()        # 转为json格式
        print(resp_data.url)                     # 打印响应URL
        print(resp_data_json)                    # 打印响应的json数据
        print(resp_data.status_code)             # 打印响应的状态码


class QueryAccountTest_NamePriceDiscountF(EntrytaskTestCase):
    '''查询余额测试用例
        登录态下
        请求参数中带name+price：用户name默认字母+数字+字符
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
        # 构造json请求数据，价格price为0，折扣discount为0
        req_data = {'user_name': 'xuzhao_test001', 'product_price': '0', 'product_discount': '0'}
        resp_data = requests.get('http://127.0.0.1:8000/query_account_get_test', params=req_data)
        resp_data_json = resp_data.json()        # 转为json格式
        print(resp_data.url)                     # 打印响应URL
        print(resp_data_json)                    # 打印响应的json数据
        print(resp_data.status_code)             # 打印响应的状态码


if __name__ == '__main__':
    QueryAccountTest_NamePriceDiscountA().debug_run()
    QueryAccountTest_NamePriceDiscountB().debug_run()
    QueryAccountTest_NamePriceDiscountC().debug_run()
    QueryAccountTest_NamePriceDiscountD().debug_run()
    QueryAccountTest_NamePriceDiscountE().debug_run()
    QueryAccountTest_NamePriceDiscountF().debug_run()

