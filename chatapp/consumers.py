from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class TestConsumers(WebsocketConsumer):

    def connect(self):
        self.room_name="chat_room"
        self.room_group_name="chat_group"
        async_to_sync(self.channel_layer.group_add)(
            self.room_name, self.room_group_name
        )
        self.accept()
        self.send(text_data=json.dumps({'status': 'connected'}))

    def receive(self, text_data):
        print (text_data)
        # pass
    def disconnect(self, *args, **kwargs ):
        print("Disconnected to the server.")