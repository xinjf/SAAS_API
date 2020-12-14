import os
import yaml
from utils.settings import DATA_PATH, operator_url


class OperateYaml(object):

    @classmethod
    def get_yaml_data(cls, datafile):
        """读取yaml文件
        :param:
        datafile: yaml的文件路径
        """
        yaml_path = os.path.join(DATA_PATH + datafile)
        with open(yaml_path, 'r', encoding='utf-8') as f:
            file_content = f.read()
        case_data = yaml.load(file_content, Loader=yaml.FullLoader)[0]
        print(case_data)
        # case_id = case_data["id"]
        url = operator_url+case_data["url"]
        headers = case_data["headers"]
        data = case_data["data"]
        check = case_data["check"]
        return url, headers, data, check

