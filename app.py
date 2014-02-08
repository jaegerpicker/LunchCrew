from tornado import ioloop, web
from tornado.escape import json_encode
from tornado.websocket import WebSocketHandler


class MainHandler(web.RequestHandler):
    def get(self):
        self.write("Hello, world?")


class ShinyHandler(WebSocketHandler):
	handlers = []

	
    def open(self):
        self.handlers.append(self)

    def on_message(self, msg):
        self.write_message(json_encode({
            'msg': 'Got it, thanks!'
    }))

    def on_close(self):
        self.handlers.remove(self)

application = web.Application([
    (r"/", MainHandler),
    (r"/socket/", ShinyHandler)
])	

if __name__ == "__main__":
    application.listen(8888)
    ioloop.IOLoop.instance().start()