import os
import time
import unittest
from package import htmltestrunner
from lib.log import info
from utils.settings import REPORT_PATH, CASES_PATH


def generate_htmlreport():
    """
    生成测试报告
    """
    time_now = time.strftime("%Y_%m_%d-%H_%M_%S_")
    htmlreport = time_now + "report.html"
    fp = open(os.path.join(REPORT_PATH, htmlreport), "wb")
    info("生成接口自动化测试报告:{0}".format(htmlreport))

    runner = htmltestrunner.HTMLTestRunner(
        stream=fp,
        verbosity=2,
        title="测试报告",
        description="用例执行情况:",
    )
    return runner


def choose_all_cases(case_suite, pattern):
    """
    获取指定路径下所有的测试用例
    :param
    pattern: 匹配模式
    case_suite: 执行的用例集，例如执行api文件的用例，即传入参数api
    case: test_case下执行的用例路径
    :return: 测试用例集"""
    # case_suite = cases_path + case_suite
    case_suite = os.path.join(CASES_PATH, case_suite)
    discover_all_cases = unittest.defaultTestLoader.discover(case_suite, pattern=pattern,
                                                             top_level_dir=None)
    return discover_all_cases









