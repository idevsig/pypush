import json
import time

from ..utils.fetch import Fetch
from ._provider import Provider


class WeCom(Provider):
    """
    企业微信通知
    """

    def __init__(self, token=''):
        self.token = token
        self.msgtype = 'text'

    def _signature(self):
        pass

    def _geturl(self):
        """
        生成请求的 URL
        :param sign: 签名
        """
        return f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={self.token}'

    def setmsgtype(self, msgtype):
        """
        设置消息类型
        :param msgtype: 消息类型
        """
        self.msgtype = msgtype if msgtype in ['text', 'markdown'] else 'text'
        return self

    def send(self, message):
        """
        发送通知
        :param message: 消息内容
        """
        req_url = self._geturl()

        headers = {
            'content-type': 'application/json',
        }
        req = Fetch()
        req.update_headers(headers)

        data = {
            'msgtype': self.msgtype,
            self.msgtype: {
                'content': message,
            },
        }
        data = json.dumps(data, indent=4)
        req.post(req_url, data=data.encode('utf-8'))
        return req.response
