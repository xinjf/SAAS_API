import hashlib
import requests
import warnings
from utils.operate_config import OperateIni
from utils.http_requests import http_requests
from utils.settings import *
import datetime


class LoginSet():

    def create_token(self):
        staff["real_operator_id"] =real_operator_id
        url = operator_url + '/api/common/login'
        res = http_requests(url, "post", staff)
        token = "bearer" + " " + res["data"]["staff"]["token"]
        nowtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        OperateIni("AM_token.ini").ini_write_value( "token", "token", token)
        OperateIni("AM_token.ini").ini_write_value("token", "time", nowtime)
        return token

    def get_token(self):
        token_all = OperateIni("AM_token.ini").ini_read_items("token")
        token = token_all["token"]
        start_time = token_all["time"]
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

if __name__=="__main__":
    LoginSet().get_token()