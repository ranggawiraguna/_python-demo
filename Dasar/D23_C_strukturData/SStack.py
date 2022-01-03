#SINGLE STACK

def masuk(varStack, temp) :
    if type(temp) is type(tuple()) :
        for nilai in temp :
            varStack.append(nilai)

    else :
        varStack.append(temp)

    print("Data {} telah dimasukkan ke dalam Stack!".format(temp))

def keluar(varStack) :
    temp = varStack.pop()
    print("Data {} telah dikeluarkan dari Stack!".format(temp))

def reset(varStack) :
    varStack.clear()
    print("Penyimpanan pada Stack telah direset!")

#Blok main hanya berfungsi pada saat file dijalankan secara independen, dan tidak akan berfungsi jika file lain malakukan import pada modul ini
if __name__ == '__main__':
    dataStack = list()

    while(True) :
        print(50*"=")
        print("Pilihan : [1]VIEW STACK\n\t\t  [2]PUSH STACK\n\t\t  [3]POP STACK\n\t\t  [4]RESET STACK\n\t\t  [0]KELUAR")
        pil = input("Pilih\t:  ")
        print(50*"=")

        if pil is '0' :
            print(50 * "=")
            exit()

        elif pil is '1' :
            if len(dataStack) == 0 :
                print("Data STACK :\n[KOSONG]")

            else :
                print("Data STACK :\n{}".format(dataStack))

        elif pil is '2' :
            masuk(dataStack, eval(input("Masukkan satu data, ..., atau lebih : ")))

        elif pil is '3' :
            keluar(dataStack)

        elif pil is '4' :
            reset(dataStack)

        else :
            print("Pilihan yang nada masukkan salah!")

        print(50*"=")
        print("\n\n")
