import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 用例路径
CASES_PATH = os.path.join(BASE_PATH, "test_case")
# 参数路径
DATA_PATH = os.path.join(BASE_PATH, "test_data")
# ini配置文件路径
CONFIG_PATH = os.path.join(BASE_PATH, "config")
# 测试报告生成路径
REPORT_PATH = os.path.join(BASE_PATH, "report")
# 日志生成路径
LOG_PATH = os.path.join(BASE_PATH, "logs")
# qa环境的资管通的url和db
operator_url = "http://staff.backend.qa-saas.heroera.com"
db_path = "qa_db"
real_operator_id = 105

# 预发布环境
# url_path = 'http://staff.backend.qa-saas.heroera.com/'
# db_path = "pre_pro_db"

# qa环境配置中心的url
