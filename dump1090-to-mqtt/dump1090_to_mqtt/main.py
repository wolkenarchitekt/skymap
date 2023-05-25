import asyncio
import json
from typing import AsyncGenerator, Dict, List

import aiohttp
import asyncio_mqtt

DUMP1090_HOST = "dump1090"
DUMP1090_PORT = "8080"
DUMP1090_URL = f"http://{DUMP1090_HOST}:{DUMP1090_PORT}/data/aircraft.json"

MOSQUITTO_HOST = "mosquitto"
MOSQUITTO_PORT = 1883


async def receive_dump1090() -> AsyncGenerator[List[Dict], None]:
    async with aiohttp.ClientSession() as session:
        while True:
            async with session.get(DUMP1090_URL) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    yield response_json["aircraft"]
                else:
                    print("Error receiving dump1090 response")
            await asyncio.sleep(1)


async def forward_dump1090():
    async with asyncio_mqtt.Client(
        hostname=MOSQUITTO_HOST, port=MOSQUITTO_PORT
    ) as mqtt_client:
        async for aircrafts in receive_dump1090():
            for aircraft in aircrafts:
                await mqtt_client.publish(
                    "traffic/dump1090", payload=json.dumps(aircraft)
                )
