import json

from ..utils.fetch import Fetch
from ._provider import Provider


class Notify(Provider):
    """
    Notify通知
    """

    def __init__(self, token='', user_id=''):
        self.token = token
        self.user_id = user_id

    def _signature(self):
        pass

    def _geturl(self):
        """
        生成请求的 URL
        """
        return 'https://notify.dev/api/v1/notify'

    def send(self, message, title=''):
        """
        发送通知
        :param message: 消息内容
        """
        req_url = self._geturl()

        headers = {
            'Content-Type': 'application/json',
            'Authorization': self.token,
        }
        req = Fetch()
        req.update_headers(headers)

        data = {
            'user_id': self.user_id,
            'title': '新消息' if title == '' else title,
            'body': message,
        }
        data = json.dumps(data, indent=4)
        req.post(req_url, data=data.encode('utf-8'))
        return req.response
