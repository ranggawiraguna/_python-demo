import socket

print(socket.socket().recv)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 1234
sock.bind((host,port))

sock.listen(1)
print("Waiting For Connection")

connection, client = sock.accept()
print(client, "Connected")
print(connection, "Connected")

while True :
    data,sender = sock.recvfrom(512)
    if not data :
        print("Continue")

    else :
        print("Received '%s'" % data)
        print(type(sender), sender)


connection.close()