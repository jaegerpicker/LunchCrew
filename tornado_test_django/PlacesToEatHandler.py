"""Place to eat http handler """
from tornado.web import RequestHandler
from tornado.gen import coroutine
from tornado.gen import Task
from tornado_test_django import settings
from AsyncDjango import AsyncDjango


class PlacesToEatHandler(RequestHandler):
    """ Handler Class """

    @coroutine
    def get(self):
        """ Returns a list of places to eat """
        a = AsyncDjango()
        pps = yield Task(a.get_place_to_eat, settings.SERIALIZER_FORMAT)
        self.write(pps)