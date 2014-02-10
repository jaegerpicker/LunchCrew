"""Tornado's main http handler """
from tornado.web import RequestHandler


class MainHandler(RequestHandler):
    """ Handler Class """

    def get(self):
        """ Returns a list of places to eat """
        self.render("index.html")
