"""生成随机字符"""
import json
import random
import string


class RandomParams:

    def random_num(self):
        return ''.join(random.sample(string.digits, 4))

    def random_str(self):
        return  ''.join(random.sample(string.ascii_letters + string.digits, 5))

    def build_random_params(self,data):
        random_str = "${random_str}"
        random_num = "${random_num}"
        if isinstance(data,dict):
            data = json.dumps(data)
        if random_str in data:
            data = data.replace(random_str,self.random_str())
        if random_num in data:
            data = data.replace(random_num,self.random_num())
        return data

# a = {"str":"${random_str}","num":"${random_num}"}
#
# print(RandomParams().build_random_params(a))




