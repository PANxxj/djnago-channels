from channels.consumer import SyncConsumer,AsyncConsumer

class MySyncconsumer(SyncConsumer):
    
    def websocket_connect(self,event):
        print("websocket_connect....",event)
        self.send({
            'type': 'websocket.accept',
        })

    def websocket_receive(self,event):
        print("websocket_receive....",event)
        
    def websocket_disconnect(self,event):
        print("websocket_disconnect....",event)


class MyAsyncconsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print("websocket_connect....",event)
        await self.send({
            'type': 'websocket.accept',
        })
        
    async def websocket_receive(self,event):
        print("websocket_receive....",event)
        
    async def websocket_disconnect(self,event):
        print("websocket_disconnect....",event)