"""Place to eat http handler """
from tornado.web import RequestHandler
from tornado.gen import coroutine
from tornado.gen import Task
from tornado_test_django import settings
import AsyncDjango


class SuggestedDatesHandler(RequestHandler):
    """ Handler Class """

    @coroutine
    def get(self):
        a = AsyncDjango()
        sds = yield Task(a.get_suggested_dates, settings.SERIALIZER_FORMAT)
        self.write(sds)

    @coroutine
    def post(self, dt):
        a = AsyncDjango()
        sds = yield Task(a.get_suggested_dates_by_date, settings.SERIALIZER_FORMAT, dt)
        self.write(sds)

    @coroutine
    def put(self, id, text, user):
        a = AsyncDjango()
        sdc = yield Task(a.add_comment_to_sgdt, settings.SERIALIZER_FORMAT, id, text, user)
        self.write(sdc)

    @coroutine
    def delete(self, id, comment):
        a = AsyncDjango()
        sdd = yield Task(a.remove_comment_from_sgdt, settings.SERIALIZER_FORMAT, id, comment)
        self.write(sdd)