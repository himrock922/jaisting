from channels.generic.websocket import WebsocketConsumer
import json
import libioc

class VNCConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        data_json = json.loads(text_data)
        try:
            jail = libioc.Jail(data_json["jail_name"])
            response = jail.exec(data_json["message"].split(" "))
        except (libioc.errors.JailNotFound):
          raise Http404('%s does not found' % data_json["jail_name"])
        self.send(text_data=response[0])