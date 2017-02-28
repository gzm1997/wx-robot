# python itchat+机器人web api实现个人微信机器人

------
本项目[github地址][1]

------
### 使用方法（前提是设备安装了python）：

本地使用：下载本项目到本地，解压，进入项目目录，输入pip install itchat，等待安装完成，输入python wx.py，用手机扫描生成的二维码，确认登陆即可

------

## 核心

 - [python itchat模块][2]
 - [图灵机器人web api][3]

本项目只有两个关键文件：

 1. wx.py

![源自wx.py][4]

```
#itchat装饰器
@itchat.msg_register(itchat.content.TEXT)
#定义消息回复函数
def text_reply(msg):
    return "柱明家的火腿：" + getResponse(msg["Text"])["text"]
```

```
#扫码登陆
itchat.auto_login(enableCmdQR=True)
```

```
#运行itchat
itchat.run()
```
 2. tuling.py

![源自tuling.py][5]




  [1]: https://github.com/15331094/wx-robot
  [2]: https://itchat.readthedocs.io/zh/latest/
  [3]: http://www.tuling123.com/help/h_cent_webapi.jhtml?nav=doc
  [4]: https://github.com/15331094/wx-robot/blob/master/screenshots/wx.png?raw=true
  [5]: https://github.com/15331094/wx-robot/blob/master/screenshots/tuling.png?raw=true
