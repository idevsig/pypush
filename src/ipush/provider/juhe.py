from ..utils.fetch import Fetch
from ._provider import Provider


class Juhe(Provider):
    """
    Juhe通知
    """

    def __init__(self, token='', service_id=''):
        self.token = token
        self.service_id = service_id
        self.doc_type = 'txt'

    def _signature(self):
        pass

    def _geturl(self):
        """
        生成请求的 URL
        """
        return 'https://tui.juhe.cn/api/plus/pushApi'

    def setdoctype(self, doc_type):
        self.doc_type = (
            doc_type if doc_type in ['html', 'markdown', 'txt', 'json'] else 'txt'
        )
        return self

    def send(self, message, title=''):
        """
        发送通知
        :param message: 消息内容
        """
        req_url = self._geturl()

        req = Fetch()

        data = {
            'token': self.token,
            'service_id': self.service_id,
            'title': '新消息' if title == '' else title,
            'content': message,
            'doc_type': self.doc_type,
        }
        req.post(req_url, data)
        return req.response
