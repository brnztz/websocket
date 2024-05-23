import socket

# Criar o socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Servidor TCP aguardando conexão...")
conn, addr = server_socket.accept()
print(f"Conectado a {addr}")

# Receber e enviar dados
data = conn.recv(1024)
print(f"Recebido: {data.decode()}")
conn.sendall(b"Resposta do servidor")

conn.close()
server_socket.close()
