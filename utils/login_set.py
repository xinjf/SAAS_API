import hashlib
import requests
import warnings
from utils.operate_config import OperateIni
from utils.http_requests import http_requests
from utils.settings import *
import datetime

# def get_token():
#     if getattr(ParamsDispose,"token") is None:
#         data = {"mobile": str(mobile), "password":str(password), "real_operator_id": real_operator_id}
#         url = operator_url + '/api/common/login'
#         res = http_requests(url,"post",data)
#         try:
#             setattr(ParamsDispose, "token", "bearer" + " " + res["data"]["staff"]["token"])
#         except ValueError as e:
#             print("获取token失败：{}".format(e))
#         return getattr(ParamsDispose,"token")
#     else:
#         return getattr(ParamsDispose,"token")


class LoginSet:

    def create_token(self):
        data = {"mobile": str(mobile), "password": str(password), "real_operator_id": real_operator_id}
        url = operator_url + '/api/common/login'
        res = http_requests(url, "post", data)
        token = "bearer" + " " + res["data"]["staff"]["token"]
        nowtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        OperateIni().ini_write_value("AM_token.ini", "token", "token", token)
        OperateIni().ini_write_value("AM_token.ini", "token", "time", nowtime)
        return token

    def get_token(self):
        token = OperateIni().ini_get_token()["token"]
        start_time = OperateIni().ini_get_token()["time"]
        end_time = (datetime.datetime.now() - datetime.timedelta(minutes=5)).strftime("%Y-%m-%d %H:%M:%S")
        if token != "":
            if start_time > end_time :
                return token
            else:
                return self.create_token()
        else:
            return self.create_token()


    def hash_md5(self,pwd):
        """MD5加密"""
        md5 = hashlib.md5()
        if pwd:
            md5.update(pwd.encode("utf-8"))
            sign = md5.hexdigest()
            return sign
        else:
            return

    def get_cookie(self,data, url):
        """根据data和url获取cookie"""
        data["password"] = self.hash_md5(data["password"])
        session = requests.session()
        cookie_jar = session.post(url=url, json=data).cookies
        cookie = requests.utils.dict_from_cookiejar(cookie_jar)
        warnings.simplefilter("ignore", ResourceWarning)
        return cookie



