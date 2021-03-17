import requests



def http_requests(url,  method, data, token=None):
    header = {"Authorization": token}
    if method.lower() == "get":
        res = requests.get(url=url, params=data,headers = header)
        return res.json()

    elif method.lower() == "post":
        res = requests.post(url=url, json=data, headers=header)
        return res.json()


