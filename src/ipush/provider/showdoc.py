import json

from ..utils.fetch import Fetch
from ._provider import Provider


class Showdoc(Provider):
    """
    Showdoc通知
    """

    def __init__(self, token=''):
        self.token = token

    def _signature(self):
        pass

    def _geturl(self):
        """
        生成请求的 URL
        """
        return f'https://push.showdoc.com.cn/server/api/push/{self.token}'

    def send(self, message, title=''):
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
            'title': '新消息' if title == '' else title,
            'content': message,
        }
        data = json.dumps(data, indent=4)
        req.post(req_url, data=data.encode('utf-8'))
        return req.response
