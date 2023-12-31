import json

from ..utils.fetch import Fetch
from ._provider import Provider


class Alertzy(Provider):
    """
    Alertzy通知
    """

    def __init__(self, token=''):
        self.token = token

    def _signature(self):
        pass

    def _geturl(self):
        """
        生成请求的 URL
        """
        return 'https://alertzy.app/send'

    def send(self, message, title=''):
        """
        发送通知
        :param message: 消息内容
        """
        req_url = self._geturl()

        req = Fetch()

        data = {
            'accountKey': self.token,
            'title': '新消息' if title == '' else title,
            'message': message,
        }
        req.post(req_url, data)
        return req.response
