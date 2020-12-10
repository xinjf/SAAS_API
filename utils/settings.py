import os
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CASES_PATH = os.path.join(BASE_PATH, "test_case")
DATA_PATH = os.path.join(BASE_PATH, "test_data")
CONFIG_PATH = os.path.join(BASE_PATH, "config")
REPORT_PATH = os.path.join(BASE_PATH, "report")
HTML_PATH = os.path.join(REPORT_PATH,"report")
LOG_PATH = os.path.join(REPORT_PATH,"logs")

operator_url = "http://staff.backend.qa-saas.heroera.com"
db_path = "qa_db"
real_operator_id = 20

# 预发布环境
# url_path = 'http://staff.backend.qa-saas.heroera.com/'
# db_path = "pre_pro_db"


