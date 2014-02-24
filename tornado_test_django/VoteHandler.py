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


    @coroutine
    def put(self, id, vote_val, user_id):
        a = AsyncDjango()
        v = yield Task(a.insert_votes, settings.SERIALIZER_FORMAT, id, vote_val, user_id)
        self.write(v)


    @coroutine
    def post(self, id, vote_val):
        a = AsyncDjango()
        v = yield Task(a.update_vote, settings.SERIALIZER_FORMAT, id, vote_val)
        self.write(v)


    @coroutine
    def delete(self, id):
        a = AsyncDjango()
        v = yield Task(a.delete_vote, settings.SERIALIZER_FORMAT, id)
        self.write(v)
