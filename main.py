import asyncio
from websockets.sync.client import connect

def listen():
    with connect("ws://192.168.10.1/traffic") as websocket:
        while True:
            message = websocket.recv()
            yield message
        

for message in listen():
    print(message)
