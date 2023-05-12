import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):

        self.room_group_name = 'test-room'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self,close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

        print('Disconnected!')

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        action = data['action']

        if (action == 'new-offer') or (action == 'new-answer'):
            receiver_channel_name = data['message']['receiver_channel_name']
            data['message']['receiver_channel_name'] = self.channel_name

            await self.channel_layer.send(
                receiver_channel_name,
                {
                    'type': 'send.sdp',
                    'data': data
                }
            )

            return

        data['message']['receiver_channel_name'] = self.channel_name

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send.sdp',
                'data': data
            }
        )

    async def send_sdp(self, event):
        data = event['data']

        await self.send(text_data=json.dumps(data))
