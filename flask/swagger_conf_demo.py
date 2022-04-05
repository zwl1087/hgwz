'''
python API 配置swagger Demo
1、定义Namespace
2、配置swagger接口文档的两种方式 @namespace.doc() 和 @api.parser()
3、两种方式的参数传递
4、定义路由及子路由
'''

from flask import Flask
from flask_restx import Resource, Api, Namespace, fields

# 【step1：实例话flask】
app = Flask(__name__)
api = Api(app, version='2.001')
# ====【在这里定义命名空间】====================================================================================================
# 【step2：定义 Namespace】

# 按照接口的个数来定义命名空间，直接展示swagger UI页面上
setTestResult_ns = Namespace("setTestResult", description="回写测试结果接口")
queryTestResult_ns = Namespace("queryTestResult", description="查询测试结果接口")
redoTestCase_ns = Namespace("redoTestCase", description="重试测试用例")


# ====【在这里定义请求接口】====================================================================================================
# 【step3：定义接口】
# /*
#    1、 一个 class 类表示一个接口，
#    2、 多个class类 可以公用一个Namespace
#    3、 共用一个Namespace 时， 可以添加子路由加以区分
# */
# namespace.doc() 方式添加接口文档
@setTestResult_ns.route("/v1")  # 添加子路由
class SetTestResult(Resource):
    # get请求添加参数接口文档
    @setTestResult_ns.doc(params={"case_id": "testcase id"})
    def get(self):
        return {"code": 0, "msg": "put result success"}

    def post(self):
        return {"code": 0, "msg": "post result success"}


post_model = api.model("post_model", {
    "case_name": fields.String(discriminator="the case name", required=True),
    "case_id": fields.Integer(min=0),
    "case_flag": fields.String(discriminator="case deal status", enum=["Y", "N"]),
})


@queryTestResult_ns.route("/result")
class QueryTestResult(Resource):
    @queryTestResult_ns.doc(body=post_model)
    def post(self):
        return {"code": 0, "data": [], "msg": "query is success"}


@queryTestResult_ns.route("/status")
class QueryTestStatus(Resource):
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


# ====【在这里定义接口路由】====================================================================================================
# 【step4：添加路由:  请求的地址】 为命名空间指定访问资源的路径
api.add_namespace(setTestResult_ns, "/setTestResult")
api.add_namespace(queryTestResult_ns, "/queryTestResult")
api.add_namespace(redoTestCase_ns, "/redoTestCase")

if __name__ == '__main__':
    # 【step5：启动服务】
    app.run(port=5008, debug=True)
