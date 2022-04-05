#!/usr/bin/python3
"""
author = zhaowenlong
project = pytestProject
date = 2021/12/16

"""

from flask import Flask, session, request, Request, make_response

app = Flask(__name__)
request: Request
app.secret_key = "key"


# --------------------------------------------------------------------------------------
@app.route("/request", methods=['POST', 'GET'])
def hello():
    query = request.args
    post = request.form
    return f"query: {query}\n" \
           f"post: {post}"


# --------------------------------------------------------------------------------------
@app.route("/session")
def session_handle():
    for k, v in request.args.items():
        session[k] = v
    # 数据添加至相应结果中
    resp = make_response({k: v for k, v in session.items()})
    for k, v in request.args.items():
        # 设置cookies
        resp.set_cookie(f"cookie_{k}", v)
    return resp


# --------------------------------------------------------------------------------------
# 通过装饰器@app.route定义路由


@app.route("/index")
def hello_world():
    return "<a> Hello World ! </a>"


# 定义动态路由
@app.route("/user/<username>")
def user_info(username):
    return f"user info: username is {username}"


# 限定动态参数的类型:
'''
参数类型： 
string: 接受任何不包含斜杠的文本
int：接受正整数
float：接受正浮点数
path：接受包含斜杠的任何文本
uuid: 接受UUID字符串
'''


@app.route("/userAge/<int:age>")
def user_age(age):
    return {"code": 0, "msg": f"user age is : {age}"}


# --------------------------------------------------------------------------------------
# http请求方式，http请求方式共有13种

@app.route("/getTestcase", methods=["get"])
def get_test_case():
    return {"code": 0, "msg": "get testcase data success"}


@app.route("/postTestcase", methods=["post"])
def post_test_case():
    return {"code": 0, "msg": "get testcase data success"}


if __name__ == '__main__':
    # 启动一个flask服务，并一直停留等待，直到程序停止
    # app.run("127.0.0.1", 5000)
    # ip 设置成0.0.0.0是，同一局域网的ip可以访问对应服务的接口
    app.run(host="0.0.0.0", port=5000, debug=True)
