import socket

stream_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 1234
server_address = ((host, port))

print("Connecting")

stream_socket.connect(server_address)

while True :
    stream_socket.sendall(input().encode())

stream_socket.close()