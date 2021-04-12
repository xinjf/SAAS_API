from logging import warning
import MySQLdb
import MySQLdb.cursors
from utils.operate_config import OperateIni


def connect_mysql(params,table):
    """连接数据库
    ：:param
    db_name: 数据库名称
    sql： 需要执行的sql语句"""
    config = eval(OperateIni("db.ini").ini_read_items("qa")["db"])
    # db = mysql.connector.connect(**config)
    db = MySQLdb.connect(
        host=config["host"],
        user=config["user"],
        passwd=config["password"],
        port=3306,
        charset="utf8")
    try:
        cursor = db.cursor()
        a = cursor.execute("select" + params +  "from" + table)
        print(a)
        data = cursor.fetchall()
        db.commit()
        db.close()
        return data
    except :
        warning("sql语句错误")



