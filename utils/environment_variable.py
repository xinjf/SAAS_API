from utils.login_set import LoginSet

class EnvironmentVariable:
    token = LoginSet().get_token()
    response = None