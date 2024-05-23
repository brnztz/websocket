import asyncio
import websockets

async def connect_client():
    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send("Hello, server!")
        response = await websocket.recv()
        print(f"Resposta do Servidor: {response}")

asyncio.get_event_loop().run_until_complete(connect_client())