import asyncio
import websockets

async def connect_client():
    async with websockets.connect("ws://localhost:8765") as websocket:
        # Enviar uma mensagem inicial ao servidor
        await websocket.send("Hello, server!")
        
        # Aguardar e exibir a resposta do servidor
        response = await websocket.recv()
        print(f"Resposta do Servidor: {response}")
        
        # Enviar mensagens adicionais em um loop
        while True:
            message = input("Digite uma mensagem para enviar ao servidor (ou 'exit' para sair): ")
            if message.lower() == 'exit':
                break
            await websocket.send(message)
            response = await websocket.recv()
            print(f"Resposta do Servidor: {response}")

asyncio.get_event_loop().run_until_complete(connect_client())
