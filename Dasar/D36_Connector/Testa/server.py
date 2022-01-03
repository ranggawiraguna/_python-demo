import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 8080
sock.bind((host,port))

print(100*"=")
try :
    print("Waiting For Connection")
    user = list()

    for i in range(2) :
        sock.listen(1)
        info = dict()
        info["connection"], info["client"] = sock.accept()
        user.append(info)

except :
    print("Connection Error!")

else :
    print(user)
    print("Connection Success!")

print(100*"=")

print(100*"=")
while True :
    for i in range(2) :
        data = user[i]["connection"].recv(512)
        print('Pesan ("', data.decode('utf-8'), sep='', end='") ')

        if str(data.decode('utf-8')) == 'exit' :
            for index in range(2) :
                user[index]["connection"].sendall("exit".encode())
                user[index]["connection"].close()

            else :
                print()
                print(100 * "=")
                exit(0)

        elif len(str(data.decode('utf-8'))) > 0 :
            if (user[i]["client"] == user[0]["client"]) :
                user[1]["connection"].sendall(data)
                print("Terkirim user-1")

            elif (user[i]["client"] == user[1]["client"]) :
                user[0]["connection"].sendall(data)
                print("Terkirim user-0")

        else:
            pass
