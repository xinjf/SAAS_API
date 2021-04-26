import json

import requests
url = "http://staff.backend.prod-saas.heroera.com/api/product/order/list?first_product_type=1&second_product_type=123&store_id=91&start_date=2021-04-01&end_date=2021-04-01&page=1&per_page=20&real_operator_id=41&order_id=1656&house_code=%E7%BA%BF%E4%B8%8B%E7%BC%96%E5%8F%B7"
header = {"Authorization": "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJkYXRhIjp7InN0YWZmX2lkIjo0NjcsInNpZ24iOiJjS2h4R29sRVNqIiwidHlwZSI6MSwicmVhbF9vcGVyYXRvcl9pZCI6NDEsImVudmlyb25tZW50IjoicHJvZCJ9fQ.IHwSo2GqXUPduiY0UrneUx_Z2suuAm9CnUdPjPdFd0V8NzS5DsJtnfNwqIa5GkXm4rfQtSYA1rF8jBpqWxi5VUAHkWgCt-LZMfFkxVTo5qobWZqMFj_1myp84lY5GG-jLA4mGGWNT-apjqUn_SNBW0zBkvcZka8hr7R-0Y350gwjNaKUFTlpoXbqsig5BKyn9WDb5c39ZyqJiY1y_UlJ5mp1dq72NNfNtx3LKKKrLj3CjyNQhy5VPz5uGW1PAIGpOaejHhpNtNB9q5Kjt_fT03Jx8Dngml6adNil9EjPdIoNaNz-QHsEUSepqVof14OKTfen_S2fm4uadFd8-xp_yQ"}

res = requests.get(url=url,headers = header)
res = res.text

res_dict = json.loads(res)
print(res_dict)