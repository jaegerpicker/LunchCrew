"""Tornado's main http handler """
from tornado.web import RequestHandler
from tornado.gen import coroutine
from tornado.gen import Task
from lunch_crew.models import PlaceToEat
import datetime


class MainHandler(RequestHandler):
    """ Handler Class """

    @coroutine
    def get(self):
        """ Get method of the class """
        a = AsyncDjango()
        pps = yield Task(a.get_place_to_eat)
        self.write("Hello I'm from tornado " + pps.place_name)


class AsyncDjango():
    def get_place_to_eat(self, callback):
        p = PlaceToEat.objects.all()[0]
        callback(p)
