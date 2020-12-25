from utils.http_requests import http_requests
from utils.login_set import LoginSet
from utils.ramdom_params import RandomParams

url = "http://operator_backend.backend.qa-stsp.heroera.com/api/staff/store"
data = '{"face_img":"","name":"员工_${random_str}","mobile":${random_phone},"email":"","sex":1,"remark":""}'
method= "post"
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MTE0NTIwNTQsImRhdGEiOnsiaWQiOjEsIm1vYmlsZSI6IjE4ODg0MTI5NTc3IiwibmFtZSI6Ilx1OGQ4NVx1N2VhN1x1N2JhMVx1NzQwNlx1NTQ1OCIsInNleCI6MSwiZW1haWwiOiIxODg3Nzc3Nzc3Nzc3QDE2My5jb20iLCJwaG90b191cmwiOiJodHRwczpcL1wveGtkLXNhYXMtYmFzZS5vc3MtY24tYmVpamluZy5hbGl5dW5jcy5jb21cL3FhLXN0c3BcLzIwMjAxMjI0XC9kXC9PNGp4YlVJc3YzZGRzT2JCVVg5N28xMXo3Z2hRQjAwRFpZWWdoYmZTLmpwZyIsInJlbWFyayI6Inh4eHh4eHh4eHh4eHgiLCJjcmVhdGVkX2F0IjoiMCIsInVwZGF0ZWRfYXQiOiIxNjA4ODAwNjQxIiwiZGVsZXRlZF9hdCI6bnVsbH19.dQM8LggGcCCo5ozxxme1map1DmLajxCZCuj2XfX32rm7QAD-kquSq8ozcOu2xFwve7_iToATZT63I8EGhKBRZeddeU1tsXfhdV87RoQUipw94S2Qmz9-fv-4RPk6obSUr6Lt0i9pei5q9z1zoHGJ_qynEfoKctnGcP6riLfWALw"
#
# for i in range(1,10):
#     data=RandomParams().build_random_params(data)
#     print(data)
#     res=http_requests(url,data =data,method=method,token=token)
#     print(res)