import pymysql
from utils.operate_config import OperateIni
from utils.settings import db_path


def connect_mysql(db_name, sql):
    """连接数据库
    ：:param
    db_name: 数据库名称
    sql： 需要执行的sql语句"""
    config = OperateIni(db_path).ini_read_items("db.ini")
    db = pymysql.connect(config["host"], config["user"], config["password"], db_name)
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    data = cursor.fetchall()
    db.close()
    return data

