"""Place to eat http handler """
from tornado.web import RequestHandler
from tornado.gen import coroutine
from tornado.gen import Task
from tornado_test_django import settings
import AsyncDjango


class SuggestedDateHandler(RequestHandler):
    """ Handler Class """

    @coroutine
    def get(self, id):
        a = AsyncDjango()
        sg = yield Task(a.get_suggested_date, id)
        self.write(sg)

    @coroutine
    def put(self, dt, user_id, place_id):
        a = AsyncDjango()
        sg = yield Task(a.insert_suggested_date, dt, user_id, place_id)
        self.write(sg)

    @coroutine
    def post(self, dt, user_id, place_id, id):
        a = AsyncDjango()
        sg = yield Task(a.update_suggested_date, dt, user_id, place_id, id)
        self.write(sg)

    @coroutine
    def delete(self, id):
        a = AsyncDjango()
        sg = yield Task(a.delete_suggested_date, id)
        self.write(sg)