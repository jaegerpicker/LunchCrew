"""Tornado's main http handler """
from tornado.web import RequestHandler
from lunch_crew.models import PlaceToEat
import datetime


class MainHandler(RequestHandler):
    """ Handler Class """
    def get(self):
        """ Get method of the class """
        pps = PlaceToEat.objects.all()[0]
        self.write("Hello I'm from tornado " + pps.place_name)
