#LINEAR QUEUE

#Import hanya berlaku pada file tersendiri, tidak akan berguna jika file ini di import oleh file lain
from collections import deque as queue

def masuk(varStack, temp) :

    if type(temp) is type(tuple()) :
        for nilai in temp :
            varStack.append(nilai)

    else :
        varStack.append(temp)

    print("Data {} telah dimasukkan ke dalam Stack!".format(temp))

def keluar(varStack) :
    temp = varStack.popleft()
    print("Data {} telah dikeluarkan dari Stack!".format(temp))

def reset(varStack) :
    varStack.clear()
    print("Penyimpanan pada Queue telah direset!")

#Blok main hanya berfungsi pada saat file dijalankan secara independen, dan tidak akan berfungsi jika file lain malakukan import pada modul ini
if __name__ == '__main__':
    dataQueue = queue()

    while(True) :
        print(50*"=")
        print("Pilihan : [1]VIEW QUEUE\n\t\t  [2]INSERT QUEUE\n\t\t  [3]DELETE QEEUE\n\t\t  [4]RESET QEEUE\n\t\t  [0]KELUAR")
        pil = input("Pilih\t:  ")
        print(50*"=")

        if pil is '0' :
            print(50 * "=")
            exit()

        elif pil is '1' :
            if len(dataQueue) == 0 :
                print("Data STACK :\n[KOSONG]")

            else :
                print("Data STACK :\n{}".format(dataQueue))

        elif pil is '2' :
            masuk(dataQueue, eval(input("Masukkan satu data, ..., atau lebih : ")))

        elif pil is '3' :
            keluar(dataQueue)

        elif pil is '4':
            reset(dataQueue)

        else :
            print("Pilihan yang nada masukkan salah!")

        print(50*"=")
        print("\n\n")
