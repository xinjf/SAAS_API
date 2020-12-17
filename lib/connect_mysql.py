import pymysql

from lib.generate_logs import info
from utils.operate_config import OperateIni
from utils.settings import db_path


def connect_mysql(sql):
    """连接数据库
    ：:param
    db_name: 数据库名称
    sql： 需要执行的sql语句"""
    config = OperateIni("db.ini").ini_read_items(db_path)
    db = pymysql.connect(config["host"], config["user"], config["password"])
    cursor = db.cursor()
    try:
        cursor.execute(sql)
    except Exception as e:
        info("sql语句执行失败：{}".format(e))
    db.commit()
    data = cursor.fetchall()
    db.close()
    return data

# print(connect_mysql("SELECT * from saas_iot.device"))
