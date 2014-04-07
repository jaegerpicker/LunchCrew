"""Address http handler """
from tornado.web import RequestHandler
from tornado.gen import coroutine
from tornado.gen import Task
from tornado_test_django import settings
import AsyncDjango


class AddressHandler(RequestHandler):
    """ Handler Class """

    @coroutine
    def get(self, id):
        a = AsyncDjango()
        address = yield Task(a.get_address, id)
        self.write(address)

    @coroutine
    def put(self, city, state, zip, lat, lon, street, street2):
        a = AsyncDjango()
        a = yield Task(a.insert_address, settings.SERIALIZER_FORMAT,  city, state, zip, lat, lon, street, street2)
        self.write(a)

    @coroutine
    def post(self, id,  city, state, zip, lat, lon, street, street2):
        a = AsyncDjango()
        address = yield Task(a.update_address, settings.SERIALIZER_FORMAT, id,  city, state, zip, lat, lon, street,
                             street2)
        self.write(address)

    @coroutine
    def delete(self, id):
        a = AsyncDjango()
        address = yield Task(a.delete_address, settings.SERIALIZER_FORMAT, id)
        self.write(address)


class AddressExtendedHandler(RequestHandler):

    @coroutine
    def get(self):
        a = AsyncDjango()
        address = yield Task(a.get_addresses, settings.SERIALIZER_FORMAT)
        self.write(address)