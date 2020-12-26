import json

from utils.http_requests import http_requests
from utils.login_set import LoginSet
from utils.ramdom_params import RandomParams




for i in range(1,2):
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MTE0Njc0ODksImRhdGEiOnsiaWQiOjEsIm1vYmlsZSI6IjE4ODg0MTI5NTc3IiwibmFtZSI6Ilx1OGQ4NVx1N2VhN1x1N2JhMVx1NzQwNlx1NTQ1OCIsInNleCI6MSwiZW1haWwiOiIxODg3Nzc3Nzc3Nzc3QDE2My5jb20iLCJwaG90b191cmwiOiJodHRwczpcL1wveGtkLXNhYXMtYmFzZS5vc3MtY24tYmVpamluZy5hbGl5dW5jcy5jb21cL3FhLXN0c3BcLzIwMjAxMjI0XC9kXC9PNGp4YlVJc3YzZGRzT2JCVVg5N28xMXo3Z2hRQjAwRFpZWWdoYmZTLmpwZyIsInJlbWFyayI6Inh4eHh4eHh4eHh4eHgiLCJjcmVhdGVkX2F0IjoiMCIsInVwZGF0ZWRfYXQiOiIxNjA4ODAwNjQxIiwiZGVsZXRlZF9hdCI6bnVsbH19.KYClVzHlNfQRFwnWZmcvwFM3_bKYb75vWbe7BNM7S_dCCwTihZT1l4CPwMaVLfbJe2uRZXp0S4pThsOnWAVji6zmDKw3oiPIVfZmnDgK_1U35bqpssj2lzycDuonXVdobomh-sGjDnrtVnnx4e3ckEQrUnzvqJFEGJw8imTazHU"
    data = '{"face_img":"","name":"员工_${random_str}","mobile":${random_phone},"email":"","sex":1,"remark":""}'
    url = "http://operator_backend.backend.qa-stsp.heroera.com/api/staff/store"
    method = "post"
    data=RandomParams().build_random_params(data)
    data = json.loads(data)
    res=http_requests(url,data =data,method=method,token=token)
    print(res)
