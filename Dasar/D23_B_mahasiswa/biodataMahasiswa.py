biodataTerinput = 0

def inputBiodata() :
    global biodataTerinput

    dataList = list()
    dataList.append(input("[>]Masukkan Nama\t\t: "))
    dataList.append(input("[>]Masukkan NIM\t\t\t: "))
    dataList.append(input("[>]Masukkan Jurusan\t\t: "))
    dataList.append(input("[>]Masukkan angkatan\t: "))

    biodataTerinput += 1

    return dataList

def tampilkanBiodata(dataList, banyak) :

    for orang in range(len(dataList)) :
        print("Orang-" + str(orang+1))

        for info in range(banyak):
            print("[>]Info-{} : {}".format((info + 1), dataList[orang][0][info]))

        print()