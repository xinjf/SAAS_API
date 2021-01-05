# import json
#
# from utils.http_requests import http_requests
# from utils.login_set import LoginSet
# from utils.ramdom_params import RandomParams
#
#
#
#
# for i in range(1,10):
#     token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MTE5MTQzNTMsImRhdGEiOnsiaWQiOjEsIm1vYmlsZSI6IjE4ODg0MTI5NTc3IiwibmFtZSI6Ilx1OGQ4NVx1N2VhN1x1N2JhMVx1NzQwNlx1NTQ1OCIsInNleCI6MiwiZW1haWwiOiIxMUAxNjMuY29tIiwicGhvdG9fdXJsIjoiaHR0cHM6XC9cL3hrZC1zYWFzLWJhc2Uub3NzLWNuLWJlaWppbmcuYWxpeXVuY3MuY29tXC9wcm9kLXVwbG9hZFwvMjAyMDEyMzBcLzNcL09MYXA3SGwzQ2FwVk9rQXljSm8yN1hFejVPWmJBNzM1ZE1hb0tJdXEuanBnIiwicmVtYXJrIjoieHh4IiwiY3JlYXRlZF9hdCI6IjE2MDkzMDc1NTYiLCJ1cGRhdGVkX2F0IjoiMTYwOTMyMjE4NCIsImRlbGV0ZWRfYXQiOm51bGx9fQ.EZvn4kReCM40SrVgmouWp7AxxY44gjAJVBEQL0fkM31OhGhnDGk79VwOKZU0pY_FOzQiRfdU5nDNyPEoFFUIZXHd5_3p_8iTrpVbvUsqpa1xfjtb93RwATi3G-1Ifrmxk2b95Y84JALSLc4tevimKfChdyC_J33J7UhJPFourJM"
#     data = '{"name":"员工_${random_str}","mobile":"${random_phone}","email":"","sex":1,"remark":"","photo_url":""}'
#     url = "http://operator_backend.backend.prod-stsp.heroera.com/api/staff/store"
#     method = "post"
#     data=RandomParams().build_random_params(data)
#     data = json.loads(data)
#     res=http_requests(url,data =data,method=method,token=token)
#     print(res)

print(isinstance("xxx",str))

