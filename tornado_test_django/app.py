"""Main application using django and tornado"""
from tornado.options import options
from tornado.options import define
import tornado.httpserver
import tornado.wsgi
import django.core.handlers.wsgi
from WebHandler import MainHandler
from PlaceToEatHandler import PlaceToEatHandler
from PlacesToEatHandler import PlacesToEatHandler
from VoteHandler import VoteHandler
from CommentHandler import CommentHandler
from SuggestedDateHandler import SuggestedDateHandler
from PlaceTypeHandler import PlaceTypeHandler
from PicsHandler import PicsHandler
from webSocketHandler import WSHandler
from tornado_test_django import settings


define('port', type=int, default=8080)


class Application(tornado.web.Application):
    def __init__(self):
        django.setup()
        wsgi_app = tornado.wsgi.WSGIContainer(
        django.core.handlers.wsgi.WSGIHandler())
        static_path = settings.STATIC_PATH
        handlers = [('/', MainHandler),
        (r'/placestoeat', PlacesToEatHandler),
        (r'/placetoeat(?:/(.*))?', PlaceToEatHandler),
        (r'/vote/([^/]+)', VoteHandler),
        (r'/comment([^/]+)', CommentHandler),
        (r'/placetype([^/]+)', PlaceTypeHandler),
        (r'/pics([^/]+)', PicsHandler),
        (r'/suggesteddate([^/]+)', SuggestedDateHandler),
        (r'/websocket([^/]+)', WSHandler),
        (r'.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app)),
        (r'/js/(.*)', tornado.web.StaticFileHandler, {'path': static_path}),
        (r'/css/(.*)', tornado.web.StaticFileHandler, {'path': static_path}),
        (r'/test/(.*)', tornado.web.StaticFileHandler, {'path': static_path}),
        ]
        tornado_settings = {
            "template_path": settings.TEMPLATE_PATH,
            "static_path": static_path,
        }
        tornado.web.Application.__init__(self, handlers, **tornado_settings)


def main():
    """Main function running the server """
    tornado_app = Application()
    server = tornado.httpserver.HTTPServer(tornado_app)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
