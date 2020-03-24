#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 7:56
# @Author  : xuzhaozhou
# @Site    :
# @Software: PyCharm

from ke.test_resources.cgiresource import KeBaseCgi

class AgencyManagerInfoCgi(KeBaseCgi):

    def __init__(self, tuin = None):
        super(AgencyManagerInfoCgi, self).__init__(tuin)
        self.name = "cgi-agency/agency/manager/info"
        self.reqdata.method = "GET"
        self.reqdata.params = {}

    def set_params(self, params):
        self.reqdata.params = params