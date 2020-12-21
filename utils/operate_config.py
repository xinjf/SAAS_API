import configparser
import os
from utils.settings import CONFIG_PATH


class OperateIni:
    def __init__(self,path):
        self.conf = configparser.ConfigParser()
        self.path = os.path.join(CONFIG_PATH, path)

    def ini_read_items(self,title):
        """读取ini文件并以字典返回对应的title所有的key、value
        path: config文件的路径
        title: ini文件内容title"""
        self.conf.read(self.path)            # "../config/db.ini"
        return dict(self.conf.items(title))

    def ini_get_value(self,title, key):
        self.conf.read(self.path)
        return self.conf.get(title, key)

    def ini_write_value(self,title, key, value):
        self.conf.read(self.path)
        self.conf.set(title, key, value)
        with open(self.path, "w+") as f:
            self.conf.write(f)



