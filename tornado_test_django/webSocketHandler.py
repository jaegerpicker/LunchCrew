"""Web Socket handler """
from tornado.websocket import WebSocketHandler

class WSHandler(WebSocketHandler):
    """WebSocket subclass """
    handlers = []

    def open(self):
        """Open the websocket connection """
        self.handlers.append(self)

    def on_message(self, msg):
        """Recieve a message on the socket """
        self.write_message(json_encode({
            'msg': 'Got it, thanks! msg ' + msg
            }))

    def on_close(self):
        """Close the Socket """
        self.handlers.remove(self)
