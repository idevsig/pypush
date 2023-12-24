import json

from ..utils.fetch import Fetch
from .notify import Notify


class Chanify(Notify):
    """
    Chanify通知
    """

    def __init__(self, token=''):
        self.token = token
        self.url = 'https://api.chanify.net'

    def signature(self):
        pass

    def seturl(self, url):
        self.url = url

    def requrl(self):
        """
        生成请求的 URL
        """
        return f'{self.url}/v1/sender/{self.token}'

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
            'text': message,
        }
        data = json.dumps(data, indent=4)
        req.post(req_url, data=data.encode('utf-8'))
        return req.response
