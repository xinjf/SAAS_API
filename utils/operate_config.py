import configparser
import os
from utils.settings import CONFIG_PATH


class OperateIni:
    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.token_path = os.path.join(CONFIG_PATH, "AM_token.ini")

    def ini_read_items(self, path, title):
        """读取ini文件并以字典返回对应的title所有的key、value
        path: config文件的路径
        title: ini文件内容title"""
        path = os.path.join(CONFIG_PATH, path)
        self.conf.read(path)            # "../config/db.ini"
        return dict(self.conf.items(title))

    def ini_get_value(self, path, title, key):

        path = os.path.join(CONFIG_PATH, path)
        self.conf.read(path)
        return self.conf.get(title, key)

    def ini_write_value(self, path, title, key, value):
        path = os.path.join(CONFIG_PATH, path)
        self.conf.read(path)
        self.conf.set(title, key, value)
        with open(self.token_path, "w+") as f:
            self.conf.write(f)

    def ini_get_token(self):
        return self.ini_read_items(self.token_path,"token")




