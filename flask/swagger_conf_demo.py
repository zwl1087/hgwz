from flask import Flask
from flask_restx import Resource, Api, Namespace, fields

app = Flask(__name__)
api = Api(app, version='2.001')

# 定义 Namespace
setTestResult_ns = Namespace("setTestResult", description="回写测试结果接口")
queryTestResult_ns = Namespace("queryTestResult", description="查询测试结果接口")
redoTestCase_ns = Namespace("redoTestCase", description="重试测试用例")


# namespace.doc() 方式添加接口文档
@setTestResult_ns.route("/v1")  # 添加子路由
class SetTestResult(Resource):
    # get请求添加参数接口文档
    @setTestResult_ns.doc(params={"case_id": "testcase id"})
    def get(self):
        return {"code": 0, "msg": "put result success"}


post_model = api.model("post_model", {
    "case_name": fields.String(discriminator="the case name", required=True),
    "case_id": fields.Integer(min=0),
    "case_flag": fields.String(discriminator="case deal status", enum=["Y", "N"]),

})


@queryTestResult_ns.route("")
class QueryTestResult(Resource):

    @queryTestResult_ns.doc(body=post_model)
    def post(self):
        return {"code": 0, "data": [], "msg": "query is success"}


# api.parser() 方式添加接口文档
@redoTestCase_ns.route("")
class RedoTestCase(Resource):
    # 定义一个parser解释器对象
    redo_parser = api.parser()
    # 通过解释器对象添加参数： location 是 request 对应的属性，get请求就是对应的args
    redo_parser.add_argument('id', type=int, location="args", required=True)
    redo_parser.add_argument("case_title", type=str, location="args", required=True)

    @redoTestCase_ns.expect(redo_parser)
    def get(self):
        return {"code": 0, "msg": "success"}


# 添加路由
api.add_namespace(setTestResult_ns, "/setTestResult")
api.add_namespace(queryTestResult_ns, "/queryTestResult")
api.add_namespace(redoTestCase_ns, "/redoTestCase")

if __name__ == '__main__':

    app.run(port=5008, debug=True)
