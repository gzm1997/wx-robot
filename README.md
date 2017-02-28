# python itchat+机器人web api实现个人微信机器人

------
本项目[github地址][1]
------

###效果图

![demo1][2]

![demo2][3]

------
### 使用方法（前提是设备安装了python）：

本地使用：下载本项目到本地，解压，进入项目目录，输入pip install itchat，等待安装完成，输入python wx.py，用手机微信描生成的二维码，确认登陆即可

------

## 核心

 - [python itchat模块][4]
 - [图灵机器人web api][5]

------

##图灵机器人apikey

在本项目中使用的是我的图灵机器人apikey,这个机器人的名字是火腿，谨纪念最后一条我亲手养大的狗仔。他的爸爸是我，妈妈是安妮海瑟薇。

你可以获取自己的图灵机器人apikey，[注册图灵机器人账号][6]，创建机器人，在机器人详情中你会看到你的专属apikey:

![apikey][7]

复制你的apikey,打开下载到本地我的github项目wx-robot，打开tuling.py文件，把下面的key的值，即7c1ccc2786df4e1685dda9f7a98c4ec9改为你自己的apikey即可。
```
data = {0
    'key'    : '7c1ccc2786df4e1685dda9f7a98c4ec9', # 如果这个Tuling Key不能用，那就换一个
    'info'   : _info, # 这是我们发出去的消息
    'userid' : 'wechat-robot', # 这里你想改什么都可以
}
```
可以登陆自己的图灵机器人账号，在我的机器人那里设置自己机器人的身份以及父母等等，挺好玩的，如下：

![setRotbot][8]

------

##关键文件
 
本项目只有两个关键文件：

 1. wx.py（负责微信登陆与响应）

![源自wx.py][9]

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
 2. tuling.py（负责发送信息给图灵机器人api，并获取机器人的回复）

![源自tuling.py][10]


  [1]: https://github.com/15331094/wx-robot
  [2]: https://github.com/15331094/wx-robot/blob/master/screenshots/demo1.png?raw=true
  [3]: https://github.com/15331094/wx-robot/blob/master/screenshots/demo2.png?raw=true
  [4]: https://itchat.readthedocs.io/zh/latest/
  [5]: http://www.tuling123.com/help/h_cent_webapi.jhtml?nav=doc
  [6]: http://www.tuling123.com/
  [7]: https://github.com/15331094/wx-robot/blob/master/screenshots/apikey.png?raw=true
  [8]: https://github.com/15331094/wx-robot/blob/master/screenshots/setRobot.png?raw=true
  [9]: https://github.com/15331094/wx-robot/blob/master/screenshots/wx.png?raw=true
  [10]: https://github.com/15331094/wx-robot/blob/master/screenshots/tuling.png?raw=true
