import json
import random
import re
from jsonpath_rw import parse
from utils.settings import real_operator_id


def deal_with_rely(data, response):
    """正则匹配"""
    pattern = re.compile(r"\$\{(.+?)}")
    params = pattern.findall(data)
    for p in params:
        case_id, path = p.split(":")
        res_json = response[int(case_id)]
        value = extract_json(res_json, path)
        data = pattern.sub(str(value), data, 1)
    data = json.loads(data)
    if "real_operator_id" in data:
        data["real_operator_id"] = real_operator_id
    return  data        # 返回的dict


def extract_json(data, path):
    """替换参数中的正则
    res_json: 字典
    path: 字符串
    """
    exe_json = parse(path)
    try:
        # data = json.loads(data)  # json转化字典
        value = [match.value for match in exe_json.find(data)]
        value = random.choice(value)
        return int(value)
    except TypeError:
        raise ValueError("未能获取有效的参数或者给予的json路径不对，请检查参数设置")

