# import json
# from utils.http_requests import http_requests
# from utils.login_set import LoginSet
# from utils.ramdom_params import RandomParams
#
#
#
#
# for i in range(1,5):
#     token = "bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTMwOTU2NDksImFkbWluX2lkIjoxLCJhZG1pbl9uYW1lIjoiYWRtaW4ifQ.AHxJE26Eg0xWIa56drjgGJ1Cd2hQs94fTJ0UIgXWle0"
#     data = {"carrier_name":"载体7","build_area":100,"carrier_province_code":120000000000,"carrier_city_code":120100000000,"carrier_district_code":120101000000,"carrier_address":"222","open_time":1610467200,"establish_time":1610467200,"operating_company":[],"unit_nature":2,"brand":"","carrier_desc":"","price_range_min":100,"price_range_max":200,"price_range_unit":1,"pics":"[{\"name\":\"u=3718703482,1601075361&fm=26&gp=0.jpg\",\"url\":\"https://xkd-saas-base.oss-cn-beijing.aliyuncs.com/qa/20210113/8/xmneVCWVclLG750SHYa9jGUgIfJ4Fm7p5ZTmbVja.jpg\",\"uid\":1610503691605,\"status\":\"success\"}]","id":13,"base_id":13}
#     url = "http://data-manage.backend.qa-saas.heroera.com/api/carrier/base/create"
#     method = "post"
#     data=RandomParams().build_random_params(data)
#     print(data)
#     res=http_requests(url,data =data,method=method,token=token)
#     print(res)
#
from lib.connect_mysql import connect_mysql

a= connect_mysql("SELECT * from saas_product.product_info where real_operator_id = 20")
print(a)