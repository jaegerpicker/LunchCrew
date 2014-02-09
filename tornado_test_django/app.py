"""Main application using django and tornado"""
from tornado.options import options
from tornado.options import define
import tornado.httpserver
import tornado.wsgi
import django.core.handlers.wsgi
from WebHandler import MainHandler
from webSocketHandler import WSHandler


define('port', type=int, default=8080)


def main():
    """Main function running the server """
    django.setup()
    wsgi_app = tornado.wsgi.WSGIContainer(
        django.core.handlers.wsgi.WSGIHandler())
    tornado_app = tornado.web.Application([('/', MainHandler),
        ('/websocket', WSHandler),
        ('.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app)),
      ])
    server = tornado.httpserver.HTTPServer(tornado_app)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
