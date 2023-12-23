import json
import time

from ..utils.fetch import Fetch
from ..utils.helper import signature
from .notify import Notify


class Dingtalk(Notify):
    """
    钉钉通知
    """

    def __init__(self, token='', secret=''):
        self.token = token
        self.secret = secret

    def signature(self):
        """
        签名
        """
        timestamp = str(round(time.time() * 1000))
        return (
            timestamp,
            '' if self.secret == '' else signature(self.secret, timestamp, 0),
        )

    def requrl(self, sign):
        """
        生成请求的 URL
        :param sign: 签名
        """
        return f'https://oapi.dingtalk.com/robot/send?access_token={self.token}{sign}'

    def send(self, message):
        """
        发送通知
        :param message: 消息内容
        """
        timestamp, sign = self.signature()
        req_url = self.requrl(
            '' if self.secret == '' else f'&timestamp={timestamp}&sign={sign}'
        )

        headers = {
            'content-type': 'application/json',
        }
        req = Fetch()
        req.update_headers(headers)

        data = {
            'msgtype': 'text',
            'text': {
                'content': message,
            },
        }
        data = json.dumps(data, indent=4)
        req.post(req_url, data=data.encode('utf-8'))
        return req.response
