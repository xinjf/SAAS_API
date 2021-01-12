from datetime import datetime
from dingtalkchatbot.chatbot import DingtalkChatbot
from utils.operate_config import OperateIni
from utils.settings import HTML_PATH
from lib.send_email import SendNewMail

class SendDingDing:
    def __init__(self):
        # 初始化机器人小丁
        # WebHook地址
        webhook = 'https://oapi.dingtalk.com/robot/send?access_token=430f1709c33d977df347f3a0d887b4e3d1465bd40d6bc5cb2007761804aa5a98'
        self.ding = DingtalkChatbot(webhook)

    def send(self):
        now_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        text = "{0}接口自动化测试报告已发送，请注意查收！".format(now_time)
        self.ding.send_text(msg=text, is_at_all=False)


if __name__ == '__main__':
    SendDingDing().send()
