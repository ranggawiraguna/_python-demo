import socket

user_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 8080
server_address = ((host, port))
user_socket.connect(server_address)

print(100*"=")
while True :
    data = user_socket.recv(512)
    data = data.decode("utf-8")

    if data == 'exit':
        user_socket.close()
        print(100*"=")
        exit(0)

    print("Akun-1 :", data, end='\n\n')

    user_socket.sendall(input("Akun-2 : ").encode())
    print()
