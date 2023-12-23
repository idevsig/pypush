import base64
import hashlib
import hmac
from urllib import parse


def signature(secret: str, timestamp: str, mode: int = 0):
    """
    使用提供的密钥、时间戳和模式生成签名。

    参数:
        secret (str): 用于生成签名的密钥。
        timestamp (str): 用作签名的时间戳。
        mode (int, optional): 生成签名时使用的模式。默认为0。

    返回:
        str: 生成的签名。

    异常:
        None
    """
    secret_enc = secret.encode('utf-8')
    string_to_sign = f'{timestamp}\n{secret}'
    string_to_sign_enc = string_to_sign.encode('utf-8')

    if mode == 0:
        hmac_code = hmac.new(
            secret_enc, string_to_sign_enc, digestmod=hashlib.sha256
        ).digest()
        return parse.quote_plus(base64.b64encode(hmac_code))

    hmac_code = hmac.new(string_to_sign_enc, digestmod=hashlib.sha256).digest()
    return base64.b64encode(hmac_code).decode('utf-8')
