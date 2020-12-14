import requests
from utils.settings import real_operator_id


def http_requests(url,  method, data, token=None):
    if method.lower() == "get":
        header = {}
        header["Authorization"] = token
        if data["real_operator_id"] is not int:
            data["real_operator_id"] = real_operator_id
        res = requests.get(url=url, params=data,headers = header)
        return res.json()
    elif method.lower() == "post":
        header = {}
        header["Authorization"] = token
        if data["real_operator_id"] is not int:
            data["real_operator_id"] = real_operator_id
        res = requests.post(url=url, json=data, headers=header)
        return res.json()


