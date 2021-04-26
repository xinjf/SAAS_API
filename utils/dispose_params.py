# utf-8
import json
import random
import re
from jsonpath_rw import parse
from lib.generate_logs import *


def deal_with_rely(data, response):
    """正则匹配"""
    pattern = re.compile(r"\$\{(.+?)}")
    params = pattern.findall(data)
    for p in params:
        try:
            case_id, path = p.split(":")
            res = response[int(case_id)]
            value = extract_json(res, path)
            data = pattern.sub(str(value), data,1)
        except ValueError:
            raise ValueError("参数格式有误；{}".format(p))
    if "null" or "None" in data:
        data = data.replace("null",'""').replace("None",'""')
    if "$_T" in data:
        data = data.replace('"$_T','').replace('$_T"','')
        data = data.replace("'",'"')
        data_dict = json.loads(data)
        return data_dict
    else:
        data = json.loads(data)
        return data  # 返回的dict


def extract_json(data, path):
    """替换参数中的正则
    res_dict: 字典
    path: 字符串${1：}
    """
    exe_json = parse(path)
    try:
        value = [match.value for match in exe_json.find(data)]
        if value == []:
            warning("动态参数取值为空：{}".format(path))
        else:
            value = random.choice(value)
            return value
    except TypeError:
        raise ValueError("未能获取有效的参数或者给予的json路径不对，请检查参数设置")





# data ='{"product_info":"$_T${1:data}$_T"}'
# res = {1:'{"data":["x","y"]}'}
# print(deal_with_rely(data,res))

# data = '{"product_info":["x", "y"]}'
# print(json.loads(data))

