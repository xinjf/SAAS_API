"""生成随机字符"""
import json
import random
import string
from lib.generate_logs import info
import time

class RandomParams:

    def random_phone(self):
        """
        :return:随机手机号
        """
        phone_front = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
                       "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
                       "186", "187", "188", "189"]
        return random.choice(phone_front) + ''.join(random.sample(string.digits, 8))

    def random_str(self):
        """
        :return:5位随机数
        """
        return ''.join(random.sample(string.ascii_letters + string.digits, 5))

    def build_random_params(self, data):
        try:
            if isinstance(data, dict):
                data = json.dumps(data)
            if "${random_str}" in data:
                data = data.replace("${random_str}", self.random_str())
            if "${random_phone}" in data:
                data = data.replace("${random_phone}", self.random_phone())
            if "${datetime}" in data:
                datetime = time.strftime("%Y-%m-%d")
                data = data.replace("${datetime}",datetime)

        except ValueError:
            info("random params isn`t json or dict")
        return data
