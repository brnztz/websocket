import socket

# Criar o socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enviar e receber dados
client_socket.sendto(b"Hello, servidor", ('localhost', 12345))
data, addr = client_socket.recvfrom(1024)
print(f"Recebido: {data.decode()}")

client_socket.close()
