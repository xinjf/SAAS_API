from datetime import datetime
from dingtalkchatbot.chatbot import DingtalkChatbot
from utils.environment_variable import EnvironmentVariable

class SendDingDing:
    def __init__(self):
        # 初始化机器人小丁
        # 测试地址
        # webhook = 'https://oapi.dingtalk.com/robot/send?access_token=430f1709c33d977df347f3a0d887b4e3d1465bd40d6bc5cb2007761804aa5a98'
        # 正式地址：
        webhook = 'https://oapi.dingtalk.com/robot/send?access_token=7c8de00eaa1e9de73554bd550e6387b71b81c06cd27484d539dbb3d4aed24f70'
        self.ding = DingtalkChatbot(webhook)

    def send(self):
        now_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        text = "{0}执行接口自动化测试;\n{1}\n测试报告已发送到邮箱,请注意查收！".format(now_time,getattr(EnvironmentVariable,"report"))
        self.ding.send_text(msg=text, is_at_all=False)


if __name__ == '__main__':
    SendDingDing().send()
