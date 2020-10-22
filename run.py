import sys
from lib.run_package import *
from lib.delete_expired_files import delete_expired_files
from lib.log import info

from utils.settings import CASES_PATH


OBJ_PATH = os.path.dirname(
    os.path.dirname(
        os.path.abspath(
            __file__
        )
    )
)
sys.path.append(OBJ_PATH)
# discover = unittest.defaultTestLoader.discover(
#     start_dir=CASES_PATH,
#     pattern='*.py'
# )


def chooseAllCases(pattern):
    """
    获取TestCases下所有的测试用例
    :param pattern: 匹配模式
    :return: 测试用例集
    """
    discover_all_cases = unittest.defaultTestLoader.discover(CASES_PATH, pattern=pattern,
                                                             top_level_dir=None)
    return discover_all_cases




if __name__ == "__main__":
    info("-----------测试开始------------------")

    generate_htmlreport().run(choose_all_cases("AssetManagement", "test*.py",))      # 执行用例
    # info("-----------发送最新的报告------------")
    # file = SendNewMail().find_new_file(report_path)                    # 查找最新的文件
    # SendNewMail.send_mail_html(file)                                   # 发送获取到的最新文件
    info("----------删除过期的报告-------------")
    delete_expired_files()                                               # 删除过期文件
    info("-------接口测试流程测试完成----------")
