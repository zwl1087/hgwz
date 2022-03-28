#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2022/1/3

"""

from mitmproxy import http, ctx
import json


class MitmRewrite:

    def response(self, flow: http.HTTPFlow):
        if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
            # 将接收到的【接口返回数据】转换成python 字典对象
            data = json.loads(flow.response.content)
            # 添加调试日志
            ctx.log.info(" |========================== 这里是调试日志 ")
            # 【篡改接口返回】第一条数据
            data["data"]["items"][0]["quote"]["name"] = "小脑斧-中国黄金"
            data["data"]["items"][0]["quote"]["current"] = '189.9999'
            data["data"]["items"][0]["quote"]["percent"] = '18.32'
            # 【篡改接口返回】第二条数据
            data["data"]["items"][1]["quote"]["current"] = '99.50'
            data["data"]["items"][1]["quote"]["percent"] = '7.54'
            # 将【篡改的数据】返回给 客户端
            flow.response.text = json.dumps(data)


addons = [
    MitmRewrite()
]




