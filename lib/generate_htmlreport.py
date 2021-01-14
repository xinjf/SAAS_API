import os
import time
from lib.generate_logs import info
from package import htmltestrunner
from utils.settings import HTML_PATH


def generate_html_report():
    """
    生成测试报告
    """
    time_now = time.strftime("%Y_%m_%d-%H_%M_%S_")
    htmlreport = time_now + "report.html"
    fp = open(os.path.join(HTML_PATH, htmlreport), "wb")
    info("生成接口自动化测试报告:{0}".format(htmlreport))

    runner = htmltestrunner.HTMLTestRunner(
        stream=fp,
        verbosity=2,
        title="测试报告",
        description="用例执行情况:",

    )
    return runner


if __name__ == "__main__":
    generate_htmlreport()
