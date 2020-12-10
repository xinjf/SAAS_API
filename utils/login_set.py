import hashlib
import requests
import warnings
from utils.params_dispose import ParamsDispose


def get_token(detail,res):
    if "登录成功" in detail:
        try:
            setattr(ParamsDispose, "token", "bearer" + " " + res["data"]["staff"]["token"])
        except ValueError as e:
            print("获取token失败：{}".format(e))

def hash_md5(pwd):
    """MD5加密"""
    md5 = hashlib.md5()
    if pwd:
        md5.update(pwd.encode("utf-8"))
        sign = md5.hexdigest()
        return sign
    else:
        return


def get_cookie(data, url):
    """根据data和url获取cookie"""
    data["password"] = hash_md5(data["password"])
    session = requests.session()
    cookie_jar = session.post(url=url, json=data).cookies
    cookie = requests.utils.dict_from_cookiejar(cookie_jar)
    warnings.simplefilter("ignore", ResourceWarning)
    return cookie


