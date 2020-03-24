# -*- coding: utf-8 -*-
'''示例测试用例
'''
#2020/03/24 QTAF自动生成

from entrytasktestproj.entrytasklib.testcase import EntrytaskTestCase

class HelloTest(EntrytaskTestCase):
    '''示例测试用例
    '''
    owner = "xuzhaozhou"
    timeout = 5
    priority = EntrytaskTestCase.EnumPriority.High
    status = EntrytaskTestCase.EnumStatus.Design
    
    def run_test(self):
        self.log_info("hello testcase")
        self.assert_equal(True, True)
    
if __name__ == '__main__':
    HelloTest().debug_run()

