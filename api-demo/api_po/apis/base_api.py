#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2022/1/16

"""
import uuid

import requests
import jsonpath

"""
对接口测试的工具的封装； 封装 request, jsonpath 等等
1、 提供一个发送请求的方法
2、提供一个jsonpath提取数据方法
"""

class BaseApi():
    _host = "https://qyapi.weixin.qq.com/cgi-bin/"

    def send(self, method, url, **kwargs):
        '''
        :param method:  接口请求方法
        :param url: 接口请求路径
        :param kwargs: 请求参数，包括 headers、Cookies、json、data、params 等待
        :return:  返回接口 response 对象
        '''
        _url = self._host + url
        r = requests.request(method, _url, **kwargs)
        return r

    @staticmethod
    def get_json_data(json_obj, expr):
        data = jsonpath.jsonpath(json_obj, expr)
        return data

    @staticmethod
    def uuid():
        return str(uuid.uuid4()).split("-")[0]

