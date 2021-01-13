import sys
from lib.choose_case import *
from lib.delete_expired_files import delete_expired_files
from lib.generate_htmlreport import generate_htmlreport
from lib.generate_logs import info
from lib.build_case import build_case
from lib.send_email import SendNewMail
from  lib.send_dingding import SendDingDing


OBJ_PATH = os.path.dirname(
    os.path.dirname(
        os.path.abspath(
            __file__
        )
    )
)
sys.path.append(OBJ_PATH)

if __name__ == "__main__":
    info("生成测试用例列表：{}".format(build_case()))
    info("-------- 开始执行用例----------------")
    generate_htmlreport().run(choose_all_cases(["AssetManagement"], "test*.py"))      # 执行用例
    # SendNewMail().send_mail_html()
    # SendDingDing().send()
    info("删除过期的报告:{}".format(delete_expired_files()))  # 删除过期文件
