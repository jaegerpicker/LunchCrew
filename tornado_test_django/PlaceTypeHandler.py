"""Place to eat http handler """
from tornado.web import RequestHandler
from tornado.gen import coroutine
from tornado.gen import Task
from tornado_test_django import settings
import AsyncDjango


class PlaceTypeHandler(RequestHandler):
    """ Handler Class """

    @coroutine
    def get(self, id):
        a = AsyncDjango()
        pt = yield Task(a.get_place_type, settings.SERIALIZER_FORMAT, id)
        self.write(pt)

    @coroutine
    def put(self, pt_name):
        a = AsyncDjango()
        pt = yield Task(a.insert_place_type, settings.SERIALIZER_FORMAT, pt_name)
        self.write(pt)

    @coroutine
    def post(self, pt_name, id):
        a = AsyncDjango()
        pt = yield Task(a.update_place_type, settings.SERIALIZER_FORMAT, pt_name, id)
        self.write(pt)

    @coroutine
    def delete(self, *args, **kwargs):
        a = AsyncDjango()
        pt = yield Task(a.delete_place_type, settings.SERIALIZER_FORMAT, id)
        self.write(pt)


class PlaceTypeExtendedHandler(RequestHandler):
    """ Handler to for extended functions
    """

    @coroutine
    def get(self):
        a = AsyncDjango()
        pt = yield Task(a.get_place_types, settings.SERIALIZER_FORMAT)
        self.write(pt)