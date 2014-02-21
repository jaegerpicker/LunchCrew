"""Place to eat http handler """
from tornado.web import RequestHandler
from tornado.gen import coroutine
from tornado.gen import Task
from tornado_test_django import settings
import AsyncDjango


class PlaceTypeHandler(RequestHandler):
    """ Handler Class """

    def get(self):
        self.write("place type")