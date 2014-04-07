"""Place to eat http handler """
from tornado.web import RequestHandler
from tornado.gen import coroutine
from tornado.gen import Task
from tornado_test_django import settings
from AsyncDjango import AsyncDjango


class PlaceToEatHandler(RequestHandler):
    """ Handler Class """

    @coroutine
    def get(self, id):
        """returns one place to eat based upon id"""
        a = AsyncDjango()
        pte = yield Task(a.get_one_place_to_eat, settings.SERIALIZER_FORMAT, id)
        self.write(pte)

    @coroutine
    def put(self, place_name, place_type_id, address_id, user_id):
        a = AsyncDjango()
        pte = yield Task(a.insert_place_to_eat, settings.SERIALIZER_FORMAT, place_name, place_type_id, address_id, user_id)
        self.write(pte)

    @coroutine
    def post(self, id, place_name, place_type_id, address_id, user_id):
        a = AsyncDjango()
        pte = yield Task(a.update_place_to_eat, settings.SERIALIZER_FORMAT, id, place_name, place_type_id, address_id, user_id)
        self.write(pte)

    @coroutine
    def delete(self, id):
        a = AsyncDjango()
        pte = yield Task(a.delete_place_to_eat, settings.SERIALIZER_FORMAT, id)
        self.write(pte)
