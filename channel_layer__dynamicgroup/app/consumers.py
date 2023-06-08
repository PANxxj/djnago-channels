from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio
import json
from asgiref.sync import async_to_sync

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print("Connecting to.......",event)
        print('this channel layer.......',self.channel_layer)
        print('this is channel name.....',self.channel_name)
        self.groupname=self.scope['url_route']['kwargs']['groupname']
        async_to_sync(self.channel_layer.group_add)(self.groupname,self.channel_name)
        self.send({
            'type':'websocket.accept',
        })
    
    def websocket_receive(self,event):
        print("Receiving........",event)
        print(event['text'])
        async_to_sync(self.channel_layer.group_send)(self.groupname,{
            'type':'chat.message',
            'message':event['text']
        })
        
    def chat_message(self,event):
        print("Receiving event  ........",event)
        self.send({
            'type':'websocket.send',
            'text':event['message']
        })
       
        
    def websocket_disconnect(self,event):
        print("Disconnecting........",event)
        print('this channel layer.......',self.channel_layer)
        print('this is channel name.....',self.channel_name)
        async_to_sync(self.channel_layer.group_discard)(self.groupname,self.channel_name)
        raise StopConsumer()
    
    
    
class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print("Connecting to.......",event)
        print('this channel layer.......',self.channel_layer)
        print('this is channel name.....',self.channel_name)
        self.groupname=self.scope['url_route']['kwargs']['groupname']
        await self.channel_layer.group_add(self.groupname,self.channel_name)
        await self.send({
            'type':'websocket.accept',
        })
    
    async def websocket_receive(self,event):
        print("Receiving........",event)
        print(event['text'])
        await self.channel_layer.group_send(self.groupname,{
            'type':'chat.message',
            'message':event['text']
        })
        
    async def chat_message(self,event):
        print("Receiving event  ........",event)
        await self.send({
            'type':'websocket.send',
            'text':event['message']
        })
       
        
    async def websocket_disconnect(self,event):
        print("Disconnecting........",event)
        print('this channel layer.......',self.channel_layer)
        print('this is channel name.....',self.channel_name)
        await self.channel_layer.group_discard(self.groupname,self.channel_name)
        raise StopConsumer()
    