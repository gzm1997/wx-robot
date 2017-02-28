import itchat
from tuling import getResponse

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
	#print(msg)
    return "柱明家的火腿：" + getResponse(msg["Text"])["text"]

itchat.auto_login(enableCmdQR=True)
itchat.run()