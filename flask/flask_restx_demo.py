'''
python 的 restful 风格的接口

'''
from flask import Flask
from flask_restx import Resource, Api, Namespace

app = Flask(__name__)
api = Api(app)

setTestResult_ns = Namespace("setTestResult", description="回写测试结果接口")


@setTestResult_ns.route("/v1")
class SetTestResult(Resource):

    def put(self):
        return {"code": 0, "msg": "put result success"}


api.add_namespace(setTestResult_ns, "/setTestResult")


# -------------------------------------------------------------------------
@api.route("/userInfo")
class UserInfo(Resource):
    # restful get请求接口
    def get(self):
        return {"code": 0, "mag": "get is success"}


@api.route("/getTestCase")
class GetTestCase(Resource):

    def post(self):
        return {"code": 0, "mag": "getTestCase is success"}


# -------------------------------------------------------------------------


if __name__ == '__main__':
    # app.run(debug=True)
    import random
    a = round(random.random()*100)

    print(a)


