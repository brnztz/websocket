import asyncio
import websockets

connected_clients = set()

async def handle_client(websocket, path):
    # Adicionar o cliente conectado à lista de clientes
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            print(f"Mensagem Recebida: {message}")
            response = f"Você disse: {message}"
            
            # Enviar a resposta de volta ao cliente
            await websocket.send(response)
            
            # Enviar a mensagem para todos os outros clientes conectados
            for client in connected_clients:
                if client != websocket:
                    await client.send(f"Outro cliente disse: {message}")
    finally:
        connected_clients.remove(websocket)

# server_ip = '0.0.0.0'
# server_port = 8765

start_server = websockets.serve(handle_client, "localhost", 8765)
# start_server = websockets.serve(handle_client, server_ip, server_port)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
