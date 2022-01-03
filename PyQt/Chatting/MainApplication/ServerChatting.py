import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 8080
sock.bind((host,port))

#Create Connection
print(203*"=")
try :
    print("Waiting For Connection\n")
    user = list()

    for i in range(2) :
        sock.listen(1)
        info = dict()
        info["connection"], info["client"] = sock.accept()
        user.append(info)

except :
    print("\nConnection Error!")

else :
    for status,info in zip(["User-1", "User-2"], user) :
        print(status, ":", info)

    print("\nConnection Success!")

#Get Message From Client
print(203*"=")
while True :
    for index in range(2):
        try :
            user[index]["connection"].settimeout(0.5)
            data = user[index]["connection"].recv(512)

        except socket.timeout :
            print(user[index]["client"], "Tidak mengirim pesan")
            continue

        else :
            data = data.decode('utf-8')
            print('Note : Pesan ("', data, sep='', end='") ')

            if (user[index]["client"] == user[0]["client"]):
                user[1]["connection"].sendall(data.encode())
                print("Terkirim ke", user[1]["client"])

            elif (user[index]["client"] == user[1]["client"]):
                user[0]["connection"].sendall(data.encode())
                print("Terkirim ke", user[0]["client"])

            print("Data ditemukan")
            break
