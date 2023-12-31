from abc import ABC
from abc import abstractmethod

"""
Provider 提供者
"""


class Provider(ABC):
    @abstractmethod
    def _signature(self):
        """
        签名
        """
        pass

    @abstractmethod
    def send(self, message):
        """
        发送通知
        :param message: 消息内容
        """
        pass
