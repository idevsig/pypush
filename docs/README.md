# ipush 使用教程

## 使用

### 1. 安装

```python
pip install ipush
```

### 2. 代码示例

- **钉钉群**

```python
from ipush import Dingtalk

notify = Dingtalk("token", "secret")
notify.send("ipush test")
```

- **飞书群**

```python
from ipush import Feishu

notify = Feishu("token", "secret")
notify.send("ipush test")
```

- **Lark 群**

```python
from ipush import Lark

notify = Lark("token", "secret")
notify.send("ipush test")
```

- **Bark**

```python
from ipush import Bark

notify = Bark("token")
notify.send("ipush test", "title")
notify.seturl("https://self-hosted")
notify.send("ipush test custom url")
```

- **Chanify**

```python
from ipush import Chanify

notify = Chanify("token")
notify.send("ipush test")
notify.seturl("https://self-hosted")
notify.send("ipush test custom url")
```

- **PushDeer**

```python
from ipush import PushDeer

notify = PushDeer("token")
notify.send("ipush test")
notify.seturl("https://self-hosted")
notify.send("ipush test custom url")
```

- **PushPlus**

```python
from ipush import PushPlus

notify = PushPlus("token")
notify.send("ipush test", "title")
```

- **Showdoc**

```python
from ipush import Showdoc

notify = Showdoc("token")
notify.send("ipush test", "title")
```

- **Xizhi**

```python
from ipush import Xizhi

notify = Xizhi("token")
notify.send("ipush test", "title")
```

- **Telegram**

```python
from ipush import Telegram

notify = Telegram("token")
notify.send("ipush test", "chat_id")
notify.seturl("https://self-hosted")
notify.send("ipush test custom url")
```

- **Alertzy**

```python
from ipush import Alertzy

notify = Alertzy("token")
notify.send("ipush test", "title")
```

- **Notify**

```python
from ipush import Notify

notify = Notify("token", "user_id")
notify.send("ipush test", "title")
```

- **Juhe**

```python
from ipush import Juhe

notify = Juhe("token", "service_id")
notify.send("ipush test", "title")
```
