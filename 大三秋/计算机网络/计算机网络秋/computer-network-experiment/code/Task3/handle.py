# coding=UTF-8
#handle.py
import hashlib
import web
import sys

class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "xxxx"#这里需要将xxxx替换成自己设置的Token
            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            # map(sha1.update, list)
            sha1.update(list[0].encode('utf-8'))
            sha1.update(list[1].encode('utf-8'))
            sha1.update(list[2].encode('utf-8'))
            hashcode = sha1.hexdigest()
            print ("handle/GET func: hashcode, signature: ", hashcode, signature)
            
            if hashcode == signature:
                return int(echostr)
            else:
                return ""
        except Exception as Argument:
            return Argument
