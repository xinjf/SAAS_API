import unittest
from lib.operate_excel_data import OperateExcel
from utils.dispose_params import deal_with_rely
from utils.http_requests import http_requests
from utils.environment_variable import EnvironmentVariable
from ddt import ddt,data
from utils.login_set import LoginSet
from lib.generate_logs import *

excel_data = OperateExcel(r"\test_data\AssetManagement\common\common.xlsx", sheet_name="Product").read_excel_data()

@ddt
class TestProduct(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.response = {}

    @data(*excel_data)
    def test_product(self,item):
        info("当前执行的测试用例是：{}".format(item["detail"]))

        data = deal_with_rely(item["data"], self.response)
        # print("请求参数：{}".format(data))
        res = http_requests(url=item["url"], data=data, method=item["method"],token=getattr(EnvironmentVariable,"token"))
        self.response[item["case_id"]] = res
        # # print("响应结果：{}".format(res))
        try:
            self.assertEqual(item["check_result"]['code'], res["code"])
            test_result = "PASS"
        except AssertionError as e:
            warning("断言错误{}".format(e))
            info("响应结果：{}".format(res))
            test_result = "Fail"
            raise e
        finally:
            OperateExcel(r"\test_data\AssetManagement\common\common.xlsx",
                            sheet_name="Product").write_excel_data(item["case_id"] + 1,str(res),test_result)


if __name__ == '__main__':
    unittest.main()
