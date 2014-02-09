from tornado import ioloop
from tornado import web
from tornado.escape import json_encode
from tornado.options import options 
from tornado.options import define
from tornado.options import parse_command_line
import tornado.httpserver
import tornado.wsgi
import django.core.handlers.wsgi

define('port', type=int, default=8080)


def main():
    wsgi_app = tornado.wsgi.WSGIContainer(django.core.handlers.wsgi.WSGIHandler())
    tornado_app = tornado.web.Application([('/', MainHandler),('/websocket', WSHandler),
        ('.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app)),
      ])
    server = tornado.httpserver.HTTPServer(tornado_app)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()