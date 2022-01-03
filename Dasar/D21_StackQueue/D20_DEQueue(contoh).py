from collections import deque

antrian = deque()
pil = ' '

while (pil!='0') :
    print(60*"=")
    print(60*"-")
    print("Pilihan : [1]PUSH\n\t\t  [2]POPLEFT\n\t\t  [3]POPRIGHT\n\t\t  [0]KELUAR")
    pil = input("Pilih   :  ")
    print(60*"-")

    print(60*"-")
    try :
        if pil is '0' :
            print(60 * "-")
            print(60 * "=")
            break;

        elif pil is '1' :
            antrian.append(eval(input("Masukkan Nilai\t: ")))
            print("Info Message\t: Data {} telah dimasukan ke dalam stack!".format(antrian[len(antrian)-1]))

        elif pil is '2' :
            nilai = antrian.popleft()
            print("Data {} telah dikeluarkan dari stack!".format(nilai))

        elif pil is '3' :
            nilai = antrian.pop()
            print("Data {} telah dikeluarkan dari stack!".format(nilai))

        else :
            print("Pilihan yang dimasukkan salah!")

    except Exception as e:
        print()
        print("[!]Error Massage\t: Proses tidak dapat dijalankan!")
        print("[!]Type Error \t\t: {}".format(str(type(e))[8:(len(str(type(e))) - 2)]))
        print("[!]Detail Error\t\t: {}".format(e))

    print(60*"-")
    print("Isi queue : ", end='')

    if len(antrian) == 0 :
        print("[ ]")

    else :
        print("[" + antrian[0], end='')
        for i in range(len(antrian)-1) :
            print(", " + str(antrian+1))
        print("]")

    print(60*"-")

    print(60*"=")
    print("\n")