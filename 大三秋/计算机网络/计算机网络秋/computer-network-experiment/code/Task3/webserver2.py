# coding=UTF-8
import werobot
import requests
import json

robot = werobot.WeRoBot(token='123456')

# @robot.text 修饰的 Handler 只处理文本消息
@robot.text
def echo(message):
    #判断如果关键词里有"天气"
    if "天气" in message.content:
        #比如输入为"天气&北京"，partition()将输入变为含有三个元素{"天气"，"&"，"北京"}数组
        ret = message.content.partition('&')
        #提取城市名
        addr = ret[2]
        #调用查询天气API，自己可以更换，网上有很多免费的API
        url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + addr
        response = requests.get(url=url)
        result=json.loads(response.text)
        #解析json
        data = result["data"]["forecast"][0]["date"]
        high = result["data"]["forecast"][0]["high"]
        fengli = result["data"]["forecast"][0]["fengli"]
        low = result["data"]["forecast"][0]["low"]
        fengxiang = result["data"]["forecast"][0]["fengxiang"]
        tian = result["data"]["forecast"][0]["type"]
        return "时间：" + data + "\n最好气温：" + high + "\n最低气温：" + low + "\n风向：" + fengxiang + "\n天气：" +tian
    else:
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
