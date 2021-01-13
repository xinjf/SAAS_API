from utils.login_set import LoginSet
from utils.operate_config import OperateIni

class EnvironmentVariable:
    token = LoginSet().get_token()
    report = None