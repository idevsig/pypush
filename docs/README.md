# ipush 使用教程

## 使用

### 1. 安装

```python
pip install ipush
```

### 2. 代码示例

- **钉钉群**

```python
from ipush.notify.dingtalk import Dingtalk

notify = Dingtalk("token", "secret")
notify.send("ipush test")
```

- **飞书群**

```python
from ipush.notify.feishu import Feishu

notify = Feishu("token", "secret")
notify.send("ipush test")
```

- **Lark 群**

```python
from ipush.notify.lark import Lark

notify = Lark("token", "secret")
notify.send("ipush test")
```

- **Bark**

```python
from ipush.notify.bark import Bark

notify = Bark("token")
notify.send("ipush test", "title")
notify.seturl("https://self-hosted")
notify.send("ipush test custom url")
```

- **Chanify**

```python
from ipush.notify.chanify import Chanify

notify = Chanify("token")
notify.send("ipush test")
notify.seturl("https://self-hosted")
notify.send("ipush test custom url")
```

- **PushDeer**

```python
from ipush.notify.pushdeer import PushDeer

notify = PushDeer("token")
notify.send("ipush test")
notify.seturl("https://self-hosted")
notify.send("ipush test custom url")
```

- **PushPlus**

```python
from ipush.notify.pushplus import PushPlus

notify = PushPlus("token")
notify.send("ipush test", "title")
```

- **Showdoc**

```python
from ipush.notify.showdoc import Showdoc

notify = Showdoc("token")
notify.send("ipush test", "title")
```

- **Xizhi**

```python
from ipush.notify.xizhi import Xizhi

notify = Xizhi("token")
notify.send("ipush test", "title")
```
