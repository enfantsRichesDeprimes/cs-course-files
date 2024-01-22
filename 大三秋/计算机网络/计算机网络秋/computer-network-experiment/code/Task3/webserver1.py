# coding=UTF-8
#webserver.py基于werobot开发框架的自定义回复功能
import werobot

robot = werobot.WeRoBot(token='xxxx')#这里需要将xxxx替换成自己设置的Token,和handle.py文件中以及配置服务器的Token一致

# @robot.text 修饰的 Handler 只处理文本消息
@robot.text
def echo(message):
    return message.content

# @robot.image 修饰的 Handler 只处理图片消息
@robot.image
def img(message):
    return message.img

@robot.text
def first(message, session):
    if 'first' in session:
        return '你之前给我发过消息'
    session['first'] = True
    return '你之前没给我发过消息'

# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()
