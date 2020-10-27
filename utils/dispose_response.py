import json
import random
import re
from jsonpath_rw import parse


def deal_with_rely(data, response):
    """正则匹配
    data : str
    response: {1:{"x":"x"}} 字典套字典
    """
    # data = json.dumps(data)   字典转化为json
    pattern = re.compile(r"\$\{(.+?)}")
    params = pattern.findall(data)
    for p in params:
        case_id, path = p.split(":")
        res_json = response[int(case_id)]
        value = extract_json(res_json, path)
        data = pattern.sub(str(value), data, 1)
    return json.loads(data)            # 返回的dict

def extract_json(data, path):
    """替换参数中的正则
    res_json: 字典
    path: 字符串
    """
    exe_json = parse(path)
    try:
        # data = json.loads(data)  # json转化字典
        value = [match.value for match in exe_json.find(data)]
        print("value:{}".format(value))
        value = random.choice(value)
        return int(value)
    except TypeError:
        raise ValueError("未能获取有效的参数或者给予的json路径不对，请检查参数设置")

# if __name__ == "__main__":
#     data = '{"id":"${2:data}","real_operator_id":105}'
#     response = {2: {"code": 200, "message": "ok", "data": 109}}
#     deal_with_rely(data,response)
