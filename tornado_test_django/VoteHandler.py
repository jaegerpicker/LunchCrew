"""Tornado's main http handler """
from tornado.web import RequestHandler
from tornado.gen import coroutine
from tornado.gen import Task
from lunch_crew.models import Votes
import datetime
from django.core import serializers
from tornado_test_django import settings


class VoteHandler(RequestHandler):
    """ Handler Class """

    @coroutine
    def get(self):
        """ Returns a list of votes for a place """
        a = AsyncDjango()
        pps = yield Task(a.get_place_to_eat, settings.SERIALIZER_FORMAT)
        self.write(pps)


class AsyncDjango():
    def get_place_to_eat(self, serializer, callback):
        p = Vote.objects.all()
        data = serializers.serialize(serializer, p)
        callback(data)
