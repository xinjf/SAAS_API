import unittest
from lib.operate_excel_data import OperateExcel
from utils.dispose_params import deal_with_rely
from utils.http_requests import http_requests
from utils.environment_variable import EnvironmentVariable
from ddt import ddt,data
from lib.generate_logs import *
from lib.connect_mysql import connect_mysql
from utils.assert_results import assert_result

excel_data = OperateExcel(r"\test_data\AssetManagement\common\common.xlsx",
                          sheet_name="Electricity_Template").read_excel_data()

@ddt
class Test_Electricity_Template(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.response = {}

    @data(*excel_data)
    def test_electricity_template(self,item):
        info("当前执行的测试用例是：{}".format(item["detail"]))

        if item["sql"] is not None:
            sql = item["sql"]
            res = connect_mysql(sql)[-1]
            self.response[item["case_id"]] = res
        else:
            data = deal_with_rely(item["data"], self.response)
            # print("请求参数：{}".format(data))
            res = http_requests(url=item["url"], data=data, method=item["method"],
                                token=getattr(EnvironmentVariable, "token"))
            self.response[item["case_id"]] = res
            # print("响应结果：{}".format(res))

        # 断言
        test_result=assert_result(item["check_result"],res)

        OperateExcel(r"\test_data\AssetManagement\common\common.xlsx",
                    sheet_name="Product").write_excel_data(item["case_id"] + 1,str(res),
                                                                    test_result)


if __name__ == '__main__':
    unittest.main()
