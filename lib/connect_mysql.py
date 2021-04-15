import MySQLdb
import MySQLdb.cursors
from lib.generate_logs import warning
from utils.operate_config import OperateIni
from utils.settings import db_path


def connect_mysql(sql):
    """连接数据库
    ：:param
    db_name: 数据库名称
    sql： 需要执行的sql语句"""
    config = eval(OperateIni("db.ini").ini_read_items("prod")["db"])
    # db = mysql.connector.connect(**config)
    db = MySQLdb.connect(
        host=config["host"],
        user=config["user"],
        passwd=config["password"],
        port=3306,
        charset="utf8",
        cursorclass=MySQLdb.cursors.DictCursor)
    try:
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        db.commit()
        db.close()
        return data
    except :
        warning("sql语句错误:{0}".format(sql))



# sql = connect_mysql("SELECT * FROM saas_product.product_info where real_operator_id = 41 ORDER BY id DESC LIMIT 1")
# print(sql)