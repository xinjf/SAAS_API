import hashlib
import requests
import warnings


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


