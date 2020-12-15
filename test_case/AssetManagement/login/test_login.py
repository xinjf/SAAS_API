import unittest
from lib.operate_excel_data import OperateExcel
from utils.dispose_response import deal_with_rely
from utils.http_requests import http_requests
from ddt import ddt,data
from utils.login_set import LoginSet
from utils.ramdom_params import RandomParams

excel_data = OperateExcel(r"\test_data\AssetManagement\login\login.xlsx", sheet_name="login").read_excel_data()

@ddt
class Test_login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.response = {}
        cls.g= globals()
        cls.g["token"] = LoginSet().get_token()

    @data(*excel_data)
    def test_01(self,item):
        print("当前执行的测试用例是：{}".format(item["detail"]))

        data = RandomParams().build_random_params(item["data"])

        data = deal_with_rely(data, self.response)

        res = http_requests(url=item["url"], data=data, method=item["method"],token=self.g["token"])
        self.response[item["case_id"]] = res

        try:
            self.assertEqual(item["check_result"]['code'], res["code"])
            Test_result = "PASS"
        except AssertionError as e:
            print("断言错误：{}".format(e))
            Test_result = "Fail"
            raise e
        finally:
            OperateExcel(r"\test_data\AssetManagement\login\login.xlsx", sheet_name="login").write_excel_data(item["case_id"] + 1,str(res),Test_result)


if __name__ == '__main__':
    unittest.main()
