"""Comments http handler """
from tornado.web import RequestHandler
from tornado.gen import coroutine
from tornado.gen import Task
from tornado_test_django import settings
import AsyncDjango


class CommentHandler(RequestHandler):
    """ Handler Class """

    @coroutine
    def get(self, id):
        a = AsyncDjango()
        c = yield Task(a.get_comment, settings.SERIALIZER_FORMAT, id)
        self.write(c)

    @coroutine
    def put(self, comment, user_id):
        a = AsyncDjango()
        c = yield Task(a.insert_comment, settings.SERIALIZER_FORMAT, comment, user_id)
        self.write(c)

    @coroutine
    def post(self, id, comment):
        a = AsyncDjango()
        c = yield Task(a.update_comment, settings.SERIALIZER_FORMAT, comment)
        self.write(c)

    @coroutine
    def delete(self, id):
        a = AsyncDjango()
        c = yield Task(a.delete_comment, settings.SERIALIZER_FORMAT, id)
        self.write(c)


class CommentsExtendedhandler(RequestHandler):

    @coroutine
    def get(self):
        a = AsyncDjango()
        c = yield Task(a.get_comments, settings.SERIALIZER_FORMAT)
        self.write(c)