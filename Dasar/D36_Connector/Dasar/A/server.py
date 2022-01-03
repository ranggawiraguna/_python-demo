import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 1233
sock.bind((host,port))

sock.listen(1)
print("Waiting For Connection")

connection, client = sock.accept()
print(client, "Connected")
print(connection, "Connected")

data = connection.recv(16)
print("Received '%s'" % data)

connection.

data = connection.recv(16)
print("Received '%s'" % data)

data = connection.recv(16)
print("Received '%s'" % data)

data = connection.recv(16)
print("Received '%s'" % data)

data = connection.recv(16)
print("Received '%s'" % data)

data = connection.recv(16)
print("Received '%s'" % data)

connection.close()