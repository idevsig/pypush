# ipush

向 APP、微信平台推送通知。
支持往 **Telegram、钉钉群、飞书群、Lark 群、Bark、Chanify、PushDeer、PushPlus、Showdoc、息知、Alertzy、Notify** 推送消息。

---

<a href="https://pypi.org/project/ipush" target="_blank">
    <img src="https://img.shields.io/pypi/v/ipush.svg" alt="Package version">
</a>

<a href="https://pypi.org/project/ipush" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/ipush.svg" alt="Supported Python versions">
</a>

## 使用说明

1. 安装依赖

```bash
pip install -U ipush
```

2. 创建 `notify` 对象，并发送消息

```python
from ipush import Dingtalk

notify = Dingtalk("token", "secret")
notify.send("iPush test")
```

## 支持平台

| 状态     | **国内**平台      | 官网                                                                                                      | 文档                                                                             | 备注         |
| :------- | :---------------- | :-------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------- | :----------- |
| ✔ **荐** | **钉钉群机器人**  | [https://open.dingtalk.com/](https://open.dingtalk.com/document/robots/customize-robot-security-settings) | -                                                                                |              |
| ✔ **荐** | **飞书群机器人**  | [https://open.feishu.cn/](https://open.feishu.cn/document/client-docs/bot-v3/add-custom-bot)              | -                                                                                |              |
| ✔ **荐** | **Lark 群机器人** | [https://open.larksuite.com/](https://open.larksuite.com/document/client-docs/bot-v3/add-custom-bot)      | -                                                                                |              |
| ✔ **荐** | **Bark**          | [https://day.app/2021/06/barkfaq/](https://day.app/2021/06/barkfaq/)                                      | -                                                                                | 仅支持 `iOS` |
| ✔        | **Chanify**       | [https://www.chanify.net/](https://www.chanify.net/)                                                      | -                                                                                | 仅支持 `iOS` |
| ✔        | **PushDeer**      | https://www.pushdeer.com/                                                                                 | -                                                                                |              |
| //       | //                | **基于微信公众号**                                                                                        | \\\\                                                                             | \\\\         |
| ✔        | **PushPlus**      | [https://www.pushplus.plus/](https://www.pushplus.plus/doc)                                               | -                                                                                |              |
| ✔        | **Showdoc**       | [https://push.showdoc.com.cn/](https://www.showdoc.com.cn/push)                                           | -                                                                                |              |
| ✔        | **息知**          | [https://xz.qqoq.net/](https://xz.qqoq.net/)                                                              | -                                                                                |              |
| ✔        | **聚合云推**      | [https://tui.juhe.cn/](https://tui.juhe.cn/docs)                                                          | 聚合推送。支持 `邮箱`、`微信公众号`、`钉钉机器人`、`WebHook`、`企业微信`、`Bark` |

| 状态     | **国外**平台 | 官网                                                                              | 文档 | 备注                                                                                                                                                 |
| :------- | :----------- | :-------------------------------------------------------------------------------- | :--- | :--------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✔ **荐** | **Telegram** | [https://core.telegram.org/bots/](https://core.telegram.org/bots/api#sendmessage) | -    | 创建[Bot](https://t.me/BotFather)后，将 Bot 添加至群组或频道，再添加[获取 ChatId 的机器人进群组](https://t.me/getmyid_bot)(可移除)，即可获得`ChatId` |
| ✔        | **Alertzy**  | [https://alertzy.app/](https://alertzy.app/)                                      | -    |                                                                                                                                                      |
| ✔        | **Notify**   | [https://notify.dev/](https://notify.dev/docs/quickstart)                         | -    | 安装手机 APP，复制设备 ID（`Settings -> Device ID`），输入到 [`Playground`](https://notify.dev/playground)，获取二维码，再使用手机 APP 扫描          |

## 开发

### 1. 前置开发环境

1. 使用 [**Rye**](https://rye-up.com/) 作为包管理工具

### 2. 开发流程

1. 安装依赖包：

```bash
# 同步
rye sync
```

2. 代码检测与格式化：

```bash
# 检测
rye run check

# 格式化
rye run format
```

3. 单元测试：

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
