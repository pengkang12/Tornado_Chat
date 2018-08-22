#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ssl
from tornado.httpserver import HTTPServer
import signal
from chatsocket.mktornado import *


def main():
    # os.environ['DJANGO_SETTINGS_MODULE'] = 'gailvlun.settings.development'
    sys.path.append('./gailvlun') # path to your project if needed
    # tornado.options.options.logging = None
    # tornado.options.parse_command_line()
    bootstrap()
    app = tornado.web.Application([(r'/ws', WebSocketHandler), ])
    LOG.info("WebSocket Server preparing")
    LOG.info(settings.SSL_CERT)
    try:
        ssl_ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)

        ssl_ctx.load_cert_chain(certfile=settings.SSL_CERT, keyfile=settings.SSL_CERT_KEY)
        # server = HTTPServer(app)
        if settings.TAG == 'PROD':
            sockets = tornado.netutil.bind_sockets(options.port)
            tornado.process.fork_processes(0)
            server = HTTPServer(app, ssl_options=ssl_ctx)
            server.add_sockets(sockets)
        else:
            server = HTTPServer(app, ssl_options=ssl_ctx)
            server.listen(options.port)

    except ssl.SSLError:
        LOG.error("SSLError")
    except ssl.CertificateError:
        LOG.error("CertificateError")

    LOG.info('Starting server on {0}'.format(options.allowed_hosts))
    signal.signal(signal.SIGINT, lambda sig, frame: shutdown())
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
