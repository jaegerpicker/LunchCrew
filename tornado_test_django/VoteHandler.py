"""Tornado's main http handler """
from tornado.web import RequestHandler
from tornado.gen import coroutine
from tornado.gen import Task
from AsyncDjango import AsyncDjango
from tornado_test_django import settings


class VoteHandler(RequestHandler):
    """ Handler Class """

    @coroutine
    def get(self, id):
        """ Returns a list of votes for a Suggested Date """
        a = AsyncDjango()
        v = yield Task(a.get_votes, settings.SERIALIZER_FORMAT, id)
        self.write(v)
