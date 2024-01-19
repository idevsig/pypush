import json
import time

from ..utils.fetch import Fetch
from ..utils.helper import signature
from ._provider import Provider


class Dingtalk(Provider):
    """
    钉钉通知
    """

    def __init__(self, token='', secret=''):
        self.token = token
        self.secret = secret
        self.msgtype = 'text'

    def _signature(self):
        """
        签名
        """
        timestamp = str(round(time.time() * 1000))
        return (
            timestamp,
            '' if self.secret == '' else signature(self.secret, timestamp, 0),
        )

    def _geturl(self, sign):
        """
        生成请求的 URL
        :param sign: 签名
        """
        return f'https://oapi.dingtalk.com/robot/send?access_token={self.token}{sign}'

    def setmsgtype(self, msgtype):
        """
        设置消息类型
        :param msgtype: 消息类型
        """
        self.msgtype = msgtype if msgtype in ['text', 'markdown'] else 'text'
        return self

    def send(self, message, title=''):
        """
        发送通知
        :param message: 消息内容
        """
        timestamp, sign = self._signature()
        req_url = self._geturl(
            '' if self.secret == '' else f'&timestamp={timestamp}&sign={sign}'
        )

        headers = {
            'content-type': 'application/json',
        }
        req = Fetch()
        req.update_headers(headers)

        data = {
            'msgtype': self.msgtype,
            self.msgtype: {
                'title': '新消息' if title == '' else title,
                'content' if self.msgtype != 'markdown' else 'text': message,
            },
        }
        data = json.dumps(data, indent=4)
        req.post(req_url, data=data.encode('utf-8'))
        return req.response
