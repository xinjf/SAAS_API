# utf-8
import json
import random
import re
from jsonpath_rw import parse
from utils.settings import real_operator_id
from lib.generate_logs import *


def deal_with_rely(data, response):
    """正则匹配"""
    pattern = re.compile(r"\$\{(.+?)}")
    params = pattern.findall(data)
    for p in params:
        case_id, path = p.split(":")
        res_dict = response[int(case_id)]
        value = extract_json(res_dict, path)
        data = pattern.sub(str(value), data, 1)
    return json.loads(data)  # 返回的dict


def extract_json(data, path):
    """替换参数中的正则
    res_dict: 字典
    path: 字符串
    """
    exe_json = parse(path)
    try:
        # data = json.loads(data)  # json转化字典
        value = [match.value for match in exe_json.find(data)]
        value = random.choice(value)
        return value
    except TypeError:
        raise ValueError("未能获取有效的参数或者给予的json路径不对，请检查参数设置")



#
# data = '{"data111":"${2:data[\'data1\']}","data222":"${2:data2}"}'
# response = {2: {"data": {"data1":{"data3":1}},"data2":{"data2":3}}}
# deal_with_rely(data,response)
