import socket

stream_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 1233
server_address = ((host, port))

print("Connecting")

stream_socket.connect(server_address)

stream_socket.sendall('A'.encode())

stream_socket.sendall('B'.encode())

stream_socket.sendall('C'.encode())
stream_socket.sendall('D'.encode())

stream_socket.sendall('E'.encode())

stream_socket.sendall('F'.encode())

stream_socket.close()