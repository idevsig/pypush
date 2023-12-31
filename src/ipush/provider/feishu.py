import json
import time

from ..utils.fetch import Fetch
from ..utils.helper import signature
from ._provider import Provider


class Feishu(Provider):
    """
    飞书通知
    """

    def __init__(self, token='', secret=''):
        self.token = token
        self.secret = secret

    def _signature(self):
        """
        签名
        """
        timestamp = str(round(time.time()))
        return (
            timestamp,
            '' if self.secret == '' else signature(self.secret, timestamp, 1),
        )

    def _geturl(self):
        """
        生成请求的 URL
        """
        return f'https://open.feishu.cn/open-apis/bot/v2/hook/{self.token}'

    def send(self, message):
        """
        发送通知
        :param message: 消息内容
        """
        timestamp, sign = self._signature()
        req_url = self._geturl()

        headers = {
            'content-type': 'application/json',
        }
        req = Fetch()
        req.update_headers(headers)

        data = {
            'timestamp': timestamp,
            'sign': sign,
            'msg_type': 'text',
            'content': {
                'text': message,
            },
        }
        data = json.dumps(data, indent=4)
        req.post(req_url, data=data.encode('utf-8'))
        return req.response
