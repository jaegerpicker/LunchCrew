"""Tornado's main http handler """
from tornado.web import RequestHandler
from tornado.gen import coroutine
from tornado.gen import Task
from lunch_crew.models import PlaceToEat
import datetime
from django.core import serializers


class MainHandler(RequestHandler):
    """ Handler Class """

    @coroutine
    def get(self):
        """ Returns a list of places to eat """
        a = AsyncDjango()
        pps = yield Task(a.get_place_to_eat, "json")
        self.write(pps)


class AsyncDjango():
    def get_place_to_eat(self, serializer, callback):
        p = PlaceToEat.objects.all()
        data = serializers.serialize(serializer, p)
        callback(data)
