import smtplib
import os
import time
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from lib.generate_logs import info
from utils.operate_config import OperateIni
from utils.settings import HTML_PATH


class SendNewMail:
    """发送邮件"""

    def find_new_file(self, file):
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

    def send_mail_html(self):
        file = self.find_new_file(HTML_PATH)
        email = OperateIni("email.ini").ini_read_items("email")

        # 发送邮箱服务器   smtpserver = '192.168.20.190'
        username = email["username"]  # 发送邮箱用户/密码
        password = email["password"]  # 邮箱授权码，需要邮箱设置里面获取
        mail_host = email["mail_host"]  # 设置smtp服务器

        # 发送邮件主题 获取2019-05-31 18:08:39格式的时间戳
        subject = '接口自动化测试报告_' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  #
        sender = email["sender"]  # 发送邮箱账号
        receiver = email["receiver"]  # 接收邮箱账号
        receivers = receiver.split(",")

        msg = MIMEMultipart('mixed')
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = "冯馨剑"  # 发件人  _format_addr('发送<%s>'%from_addr)
        msg['To'] = ",".join(receivers)  # 多个接收人
        # msg['To'] = receiver            # 单个接收人

        # 读取html文件内容
        with open(file, 'rb') as f:
            mail_body = f.read().decode("utf8")

        # 构造正文
        msg_html1 = MIMEText(mail_body, 'html', 'utf-8')
        msg.attach(msg_html1)

        # 构造html
        msg_html = MIMEText(mail_body, 'html', 'utf-8')
        msg_html["Content-Disposition"] = 'attachment; filename="TestReport.html"'
        msg.attach(msg_html)


        # 构造图片链接
        # sendimagefile = open(r'D:\pythontest\testimage.png', 'rb').read()
        # image = MIMEImage(sendimagefile)
        # image.add_header('Content-ID', '<image1>')
        # image["Content-Disposition"] = 'attachment; filename="testimage.png"'
        # msg.attach(image)

        try:
            smtp = smtplib.SMTP()
            smtp.connect(mail_host, 25)
            smtp.login(username, password)
            smtp.sendmail(sender, receivers, msg.as_string())
            info("邮件已发送到：{}的邮箱！".format(receiver))
        except smtplib.SMTPException as e:
            info("邮件发送失败:{}！".format(e))
if __name__=="__main__":
    SendNewMail().send_mail_html()