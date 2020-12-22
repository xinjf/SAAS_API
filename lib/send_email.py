import smtplib
import os
import time
from email.mime.text import MIMEText
from email.header import Header
from lib.generate_logs import info
from utils.operate_config import OperateIni
# from lib.settings import report_path


class SendNewMail:
    """发送邮件"""
    @classmethod
    def find_new_file(cls, file):
        file_lists = os.listdir(file)
        try:
            file_lists.sort(key=lambda fn: os.path.getmtime(
                file + "\\" + fn)
                if not os.path.isdir(file + "\\" + fn) else 0)
            file = os.path.join(file, file_lists[-1])
            info("获取最新的html报告：{0}".format(file))
            return file
        except Exception as error:
            info(error)

    @classmethod
    def send_mail_html(cls, file):
        email = OperateIni("email.ini").ini_read_items( "email")
        sender = email["sender"]  # 发送邮箱账号
        receiver = email["receiver"]     # 接收邮箱账号
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 获取2019-05-31 18:08:39格式的时间戳
        subject = '接口自动化测试报告_' + t  # 发送邮件主题
        # 发送邮箱服务器   smtpserver = '192.168.20.190'
        username = email["username"]    # 发送邮箱用户/密码
        password = email["password"]    # 邮箱授权码，需要邮箱设置里面获取
        mail_host = email["mail_host"]  # 设置smtp服务器
        # print(sender, receiver, username, password, mail_host)
        with open(file, 'rb') as f:  # 读取html文件内容
            mail_body = f.read().decode("utf-8")
        msg = MIMEText(mail_body, _subtype = 'report', _charset = 'utf-8')
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = "冯馨剑"          # 发件人
        msg['To'] = receiver            # 接收人
        try:
            smtp = smtplib.SMTP()
            smtp.connect(mail_host, 25)
            smtp.login(username, password)
            smtp.sendmail(sender, receiver, msg.as_bytes())
            info("邮件已发送到：{}的邮箱！".format(receiver))
        except smtplib.SMTPException:
            info("邮件发送失败！")


