import socket

# Criar o socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))

print("Servidor UDP aguardando mensagem...")
data, addr = server_socket.recvfrom(1024)
print(f"Recebido de {addr}: {data.decode()}")

server_socket.sendto(b"Resposta do servidor", addr)
server_socket.close()
