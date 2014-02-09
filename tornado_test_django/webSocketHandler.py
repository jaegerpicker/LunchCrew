from tornado.websocket import WebSocketHandler


class WSHandler(WebSocketHandler):
	handlers = []

	
    def open(self):
        self.handlers.append(self)

    def on_message(self, msg):
        self.write_message(json_encode({
            'msg': 'Got it, thanks!'
    }))

    def on_close(self):
        self.handlers.remove(self)