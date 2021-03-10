from lib.generate_logs import *


def assert_result(check_result,res):
    for keys in check_result:
        if (keys in res) & (res[keys]==check_result[keys]):
            return "pass"
        else:
            warning("断言失败，响应结果为：{}".format(res))
            return "fail"

