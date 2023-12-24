import json

from ..utils.fetch import Fetch
from .notify import Notify


class Bark(Notify):
    """
    Bark通知
    """

    def __init__(self, token=''):
        self.token = token
        self.url = 'https://api.day.app'

    def signature(self):
        pass

    def seturl(self, url):
        self.url = url

    def requrl(self):
        """
        生成请求的 URL
        """
        return f'{self.url}/push'

    def send(self, message):
        """
        发送通知
        :param message: 消息内容
        """
        req_url = self.requrl()

        headers = {
            'content-type': 'application/json',
        }
        req = Fetch()
        req.update_headers(headers)

        data = {
            'body': message,
            'device_key': self.token,
        }
        data = json.dumps(data, indent=4)
        req.post(req_url, data=data.encode('utf-8'))
        return req.response
