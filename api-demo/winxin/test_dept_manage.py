#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2022/1/9

"""
import requests
from uuid import uuid4
import jsonpath


class TestDeptManage():

    def setup_class(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        param = {
            # 企业ID
            # 测试公司
            # "corpid": "ww9dc9b0c15d8663a6",
            "corpid": "ww2b15141e109c9791",
            # 测试公司
            # "corpsecret": "TomXTHsd_0naqWQYvRw5s-xNetlIWSHMiVkeAYDMDJk"
            "corpsecret": "yOenVArAqlafGKOLSTSFosdihjoMIja3OkR-O4PhcSY"
        }
        r = requests.get(url, params = param)
        self.access_token = r.json()["access_token"]

    # 创建部门
    def test_create_company(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create"
        # ?access_token={self.access_token}
        uuid = str(uuid4()).split("-")[0]
        # print(uuid)
        param = {
            "access_token": self.access_token
        }
        data = {
            "name": f"广州研发中心_{uuid}",
            "name_en": f"RDGZ_{uuid}",
            "parentid": 1
            # "order": 2,
            # "id": 4
        }
        r = requests.request("post", url, params = param, json = data)
        assert r.json()["errcode"] == 0 and r.json()["errmsg"] == "created"

    # 查询部门
    def test_query_company(self):
        _id = ""
        # url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.access_token}&id={id}"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list"
        param = {
            "access_token": self.access_token
            # "id": _id
        }
        r = requests.request("get", url, params = param)
        print(r.json())
        res = jsonpath.jsonpath(r.json(), "$..name")
        print(res)
        assert r.json()['errcode'] == 0 and r.json()['errmsg'] == "ok"

    # 更新部门
    def test_update_company(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.access_token}"
        data = {
            "id": 2,
            "name": "广州研发中心_update",
            "name_en": "RDGZ_update",
            "parentid": 1,
            "order": 1
        }
        r = requests.request("post", url, json = data)
        print(r.json())

    # 删除部门
    def test_delete_company(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.access_token}&id=5"

        r = requests.request("get", url)
        print(r.json())
