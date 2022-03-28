#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2022/1/3

"""

from mitmproxy import http


class MitmMapLocal:

    # maplocal 用 request 事件来进行mock的： 客户端和 mock 的交互
    def request(self, flow: http.HTTPFlow):

        # 定义匹配条件： 这里是用url 来进行匹配的
        if "quote.json" in flow.request.pretty_url:
            # 打开本地的json 文件，该文件就是 request 的响应结果体
            with open("mitm_maplocal_response.json", encoding = "utf-8") as f:
                #  构造一个响应结果 response
                flow.response = http.Response.make(
                    200,  # 响应状态码
                    f.read(),  # 响应内容
                    {"Content-Type": "application/json"}  # 响应头信息
                )


addons = [
    MitmMapLocal()
]

