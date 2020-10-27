import requests


def http_requests(url,  method, data, token=None):
    if method.lower() == "get":
        header = {'Content-Type': 'application/json'}
        header["Authorization"] = token
        res = requests.get(url=url, params=data,headers = header)
        return res.json()
    elif method.lower() == "post":
        header = {'Content-Type': 'application/json'}
        header["Authorization"] = token
        res = requests.post(url=url, json=data, headers=header)
        return res.json()


