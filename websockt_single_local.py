#!/usr/bin/python
# -*- coding: utf-8 -*-

import jwt
import websocket
import thread
import ssl
import gevent
import json
import logging
import urllib2
from gevent import monkey

monkey.patch_all(time=True)
logging.basicConfig()

hostname = '127.0.0.1'


def on_message(ws, message):
    print(message)
    pass


def on_error(ws, error):
    print(error)
    pass


def on_close(ws):
    print("### closed ###")


def on_ping(ws, message):
    print("on ping!!!"+message)
    pass


def on_open(ws):

    def run(*args):
        for i in range(1, 60):
            gevent.sleep(1)
            ws.send('{"target": "user:305","payload": "'+str(i)+'","type": "txt"}')
            #gevent.sleep(1)
            # ws.send('{"target":"room:145","payload":" fsdffds","type":"txt"}')
        ws.close()
    thread.start_new_thread(run, ())


def main(res):
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://" + hostname + ":8888/ws?id="+str(res['id'])+"&&token="+res['token'],
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close,
                                on_ping=on_ping,
                                )

    ws.on_open = on_open
    # ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
    ws.run_forever(ping_interval=100, sslopt={"cert_reqs": ssl.CERT_NONE})


if __name__ == "__main__":

    req = urllib2.Request('http://' + hostname + '/mlogin/')
    req.add_header('Content-Type', 'application/json')
    data = {
        "mobile": "12313123",
        "password": jwt.encode({'password': '123456'}, '67ef9c880f8e33966d60d612d32562301f343c3b', algorithm='HS256')
    }
    response = urllib2.urlopen(req, json.dumps(data))
    result = json.loads(response.read())
    res = {
        'id': 304,
        'token': result['token']
    }
    main(res)

