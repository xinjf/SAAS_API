import unittest
from lib.operate_excel_data import OperateExcel
from utils.dispose_response import deal_with_rely
from lib.http_requests import http_requests
from ddt import ddt,data

from utils.params_dispose import ParamsDispose

excel_data = OperateExcel("\\AssetManagement\\login\\login.xlsx", sheet_name="登录").read_excel_data()

@ddt
class TestFirmAdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.response = {}

    @data(*excel_data)
    def test_01(self,item):
        print("当前执行的测试用例是：{}".format(item["detail"]))
        item["data"] = deal_with_rely(item["data"], self.response)

        res = http_requests(url=item["url"], data=item["data"], method=item["method"],token=getattr(ParamsDispose, "token"))
        self.response[item["case_id"]] = res

        try:
            self.assertEqual(item["check_result"]['code'], res["code"])
            Test_result = "PASS"
        except AssertionError as e:
            print("断言错误：{}".format(e))
            Test_result = "Fail"
            raise e
        finally:
            OperateExcel("\\AssetManagement\\login\\login.xlsx", sheet_name="登录").write_excel_data(item["case_id"] + 1,
                                                                                                   str(res),
                                                                                                   Test_result)




if __name__ == '__main__':
    unittest.main()
