import os
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CASES_PATH = os.path.join(BASE_PATH, "test_case")
DATA_PATH = os.path.join(BASE_PATH, "test_data")
CONFIG_PATH = os.path.join(BASE_PATH, "config")
REPORT_PATH = os.path.join(BASE_PATH, "report")
HTML_PATH = os.path.join(REPORT_PATH,"report")
LOG_PATH = os.path.join(REPORT_PATH,"logs")




# qa环境
# operator_url = "http://staff.backend.qa-saas.heroera.com"
# db_path = "qa"
# real_operator_id = 20
# staff = {"mobile":"18884129577","password":"18884129577"}



# 预发布环境
db_path = "prod"
operator_url = "http://staff.backend.prod-saas.heroera.com"
real_operator_id = 41
staff = {"mobile":"18884129577","password":"18884129577"}

