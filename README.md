# Tornado_Chat

This chat server based google's tornado aims to support high concurrency. Because Google's Tornado web server has a very high performance at high concurrency because it makes full use of conroutine.

Based this, I developed a program to use chat occassion. My program can promise that the received message can be correctly, ordered to send clients. When clients receive his own message, he must reply a sequence to tell server he has received message. Otherwise, server will resend message to client to keep message order. This mechanism guarantees message can be received.

I use redis to store message and sequence. Because redis has better performance. However, redis is unreliable. I think this is tradeoff.

I also use Django to verify client's identity.

### requirement.txt
your environment need to satisfy the requirements.

pip install -r requirement.txt 

### websocket_server

websocket_server.py is server's program.

and websocket_single_local.py is client.

##### start server
python websocket_server.py

### client

websocket_single_local.py is a client's demo.

##### start client

python websocket_local.py

##### pay attention
to client, If your program support websocket, then you can use or reference this server's program. 

### other files

I just want to package this program, so I do some experiments. 

Thank you read this.
