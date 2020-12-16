import requests
from utils.settings import real_operator_id


def http_requests(url,  method, data, token=None):
    header = {}
    if method.lower() == "get":
        header["Authorization"] = token
        res = requests.get(url=url, params=data,headers = header)
        return res.json()

    elif method.lower() == "post":
        header["Authorization"] = token
        res = requests.post(url=url, json=data, headers=header)
        return res.json()


