"""Main application using django and tornado"""
from tornado.options import options
from tornado.options import define
import tornado.httpserver
import tornado.wsgi
import django.core.handlers.wsgi
from WebHandler import MainHandler
from webSocketHandler import WSHandler
from tornado_test_django import settings


define('port', type=int, default=8080)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [('/', MainHandler), 
        ('/websocket', WSHandler),
        ('.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app)),]
        tornado_settings = {
            "template_path": settings.TEMPLATE_PATH,
            "static_path": settings.STATIC_PATH,
        }
        tornado.web.Application.__init__(self, handlers, **tornado_settings)


def main():
    """Main function running the server """
    django.setup()
    wsgi_app = tornado.wsgi.WSGIContainer(
        django.core.handlers.wsgi.WSGIHandler())
    tornado_app = Application()
    server = tornado.httpserver.HTTPServer(tornado_app)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
