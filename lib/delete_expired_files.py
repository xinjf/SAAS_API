# -*- coding: utf-8 -*-
import datetime
import os
import time
from lib.log import info
from utils.settings import REPORT_PATH,LOG_PATH


def delete_expired_files():
    """删除过期文件"""
    file_list = [REPORT_PATH, LOG_PATH]
    today = datetime.datetime.now()
    offset = datetime.timedelta(days=-7)        # days参数，删除多少天的文件
    re_date = (today + offset)
    re_date_unix = time.mktime(re_date.timetuple())
    try:
        while file_list:
            path = file_list.pop()
            for item in os.listdir(path):
                path2 = os.path.join(path, item)
                if os.path.isfile(path2):
                    if os.path.getmtime(path2) <= re_date_unix:
                        os.remove(path2)
                        info('删除文件{}'.format(path2))
                else:
                    if not os.listdir(path2):     # 判断是否为空目录
                        os.removedirs(path2)      # 删除空目录
                        info('删除空目录{}'.format(path2))
                    else:
                        file_list.append(path2)   # 获取多层文件夹的数据
                        # print("file_list:", file_list)
                    if not os.listdir(path2):
                        os.removedirs(path2)
                        info('删除空目录{}'.format(path2))
                    else:
                        file_list.append(path2)

        return True
    except Exception as e:
        return e

# delete_expired_files()

