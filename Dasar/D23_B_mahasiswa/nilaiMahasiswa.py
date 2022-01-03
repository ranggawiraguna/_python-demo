nilaiTerinput = 0

def inputNilai(banyak) :
    global nilaiTerinput

    dataList = list()

    for i in range(banyak) :
        dataList.append(input("[>]Masukkan Nilai-{}\t\t: ".format(i+1)))

    nilaiTerinput += 1

    return dataList

def tampilkanSemuaNilai(dataList):

    for orang in range(len(dataList)) :
        print("Orang-" + str(orang+1))

        for nilai in range(len(dataList[orang][1])):
            print("[>]Nilai-{} : {}".format((nilai + 1), dataList[orang][1][nilai]))

        print()