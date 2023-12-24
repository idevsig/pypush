# ipush 使用教程

## 使用

1. **钉钉群**

```python
from ipush.notify.dingtalk import Dingtalk

notify = Dingtalk("token", "secret")
notify.send("ipush test")
```

2. **飞书群**

```python
from ipush.notify.feishu import Feishu

notify = Feishu("token", "secret")
notify.send("ipush test")
```

3. **Lark 群**

```python
from ipush.notify.lark import Lark

notify = Lark("token", "secret")
notify.send("ipush test")
```

4. **Bark**

```python
from ipush.notify.bark import Bark

notify = Bark("token")
notify.send("ipush test")
notify.seturl("https://self-hosted")
notify.send("ipush test custom url")
```

5. **Chanify**

```python
from ipush.notify.chanify import Chanify

notify = Chanify("token")
notify.send("ipush test")
notify.seturl("https://self-hosted")
notify.send("ipush test custom url")
```

6. **PushDeer**

```python
from ipush.notify.pushdeer import PushDeer

notify = PushDeer("token")
notify.send("ipush test")
notify.seturl("https://self-hosted")
notify.send("ipush test custom url")
```
