from datetime import time
import html2text as ht
from lib.send_email import SendNewMail
from dingtalkchatbot.chatbot import DingtalkChatbot
from utils.settings import HTML_PATH
from package.htmltestrunner import _TestResult


class SendDingDing:
    def __init__(self):
        # 初始化机器人小丁
        # WebHook地址
        webhook = 'https://oapi.dingtalk.com/robot/send?access_token=430f1709c33d977df347f3a0d887b4e3d1465bd40d6bc5cb2007761804aa5a98'
        self.ding = DingtalkChatbot(webhook)

    def send(self):
        file = r'C:\Users\pujun\Desktop\APIAuto_unittest\report\report\2020_11_03-19_22_53_report.html'
        with open(file, "rb") as f:
            text = f.read().decode("utf-8")
        self.ding.send_text(msg=text, at_mobiles=["18884129577"], is_at_all=False, )


if __name__ == '__main__':
    SendDingDing().send()
