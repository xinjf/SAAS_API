import MySQLdb
import MySQLdb.cursors
from lib.generate_logs import info
from utils.operate_config import OperateIni
from utils.settings import db_path


def connect_mysql(sql):
    """连接数据库
    ：:param
    db_name: 数据库名称
    sql： 需要执行的sql语句"""
    config = eval(OperateIni("db.ini").ini_read_items(db_path)["db"])
    # db = mysql.connector.connect(**config)
    db = MySQLdb.connect(
        host=config["host"],
        user=config["user"],
        passwd=config["password"],
        port=3306,
        charset="utf8",
        cursorclass=MySQLdb.cursors.DictCursor)
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    # except Exception as e:
    #     info("sql语句{0}执行失败：{1}".format(sql,e))
    db.commit()
    db.close()
    return data

# sql = connect_mysql("SELECT * from saas_product.product_info where real_operator_id = 20")
# print(sql)