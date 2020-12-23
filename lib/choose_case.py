import os
import unittest
from utils.settings import CASES_PATH


def choose_all_cases(case_suite, pattern):
    """
    获取指定路径下所有的测试用例
    :param
    pattern: 匹配模式
    case_suite: 执行的用例集，例如执行api文件的用例，即传入参数api
    case: test_case下执行的用例路径
    :return: 测试用例集"""
    for cases in case_suite:
        case_suite = os.path.join(CASES_PATH, cases)
        discover_all_cases = unittest.defaultTestLoader.discover(case_suite, pattern=pattern,
                                                             top_level_dir=None)
        suite = unittest.TestSuite()
        suite.addTest(discover_all_cases)
        return suite



