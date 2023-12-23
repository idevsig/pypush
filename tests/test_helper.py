from urllib.parse import unquote

from ipush.utils.helper import signature


class TestHelper:
    def test_helper_dingtalk(self):
        timestamp = '1703172934000'
        dingtalk = 'aCvJuxhHC5I89JuWhmbWXa7HjbCNOzFN/YMw++xLk7Y='
        result = signature('dingtalk', timestamp, 0)
        assert unquote(result) == dingtalk

    def test_helper_feishu(self):
        timestamp = '1703172707'
        feishu = 'NnJCAEJ4jixMBRllUd+3O9Dnn8XBOxGBLivSsrcBRT4='
        result = signature('feishu', timestamp, 1)
        assert unquote(result) == feishu
