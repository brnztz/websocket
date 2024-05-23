import socket

# Criar o socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# Enviar e receber dados
client_socket.sendall(b"Hello, servidor")
data = client_socket.recv(1024)
print(f"Recebido: {data.decode()}")

client_socket.close()
