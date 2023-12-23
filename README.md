# ipush

APP 推送通知

## 使用说明

1. 安装依赖

```shell
pip install -U ipush
```

2. 创建 `notify` 对象，并发送消息

```python
from ipush.notify.dingtalk import Dingtalk
from ipush.notify.feishu import Feishu
from ipush.notify.lark import Lark

notify = Dingtalk("token", "secret")
notify.send("ipush test")

notify = Feishu("token", "secret")
notify.send("ipush test")

notify = Lark("token", "secret")
notify.send("ipush test")
```

## 支持平台

| 状态     | **国内**平台      | 官网                                                                                                      | 文档 | 备注 |
| :------- | :---------------- | :-------------------------------------------------------------------------------------------------------- | :--- | :--- |
| ✔ **荐** | **钉钉群机器人**  | [https://open.dingtalk.com/](https://open.dingtalk.com/document/robots/customize-robot-security-settings) | -    |      |
| ✔ **荐** | **飞书群机器人**  | [https://open.feishu.cn/](https://open.feishu.cn/document/client-docs/bot-v3/add-custom-bot)              | -    |      |
| ✔ **荐** | **Lark 群机器人** | [https://open.larksuite.com/](https://open.larksuite.com/document/client-docs/bot-v3/add-custom-bot)      | -    |      |

## 前置环境

1. 使用 [**Rye**](https://rye-up.com/) 作为包管理工具

## 单元测试

```bash
# rye test
rye run tests

# pytest
python -m pytest

# 打印测试报告
python -m pytest -s
```

## 仓库镜像

- https://git.jetsung.com/idev/pypush
- https://framagit.org/idev/pypush
- https://github.com/idevsig/pypush
