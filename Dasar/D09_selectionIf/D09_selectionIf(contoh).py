#SelectionIf

import os

loop = 'Y'

while (loop is 'y') or (loop is 'Y') :
    os.system('cls')
    print(65*"=")
    nilai = int(input("[>]Masukkan Nilai Akhir(angka) : "))

    if nilai > 100 :
        print("[>]Nilai Anda masukkan salah!")

    elif 56 <= nilai <= 100 :
        print("[>]Anda lulus dalam mata kuliah tersebut!")

    else :
        print("[>]Anda gagal dalam mata kuliah tersebut!")

    print(65*"=")
    nilai = input("[>]Masukkan Nilai Akhir(predikat) : ")

    if nilai in 'aAbBcC' :
        print("[>]Anda lulus dalam mata kuliah tersebut!")
        if (nilai is 'a') or (nilai is 'A') :
            print("[>]Dengan Keterangan Nilai Sangat Baik")
        elif (nilai is 'b') or (nilai is 'B') :
            print("[>]Dengan Keterangan Baik")
        elif (nilai is 'a') or (nilai is 'A') :
            print("[>]Dengan Keterangan Nilai Cukup")

    else :
        print("[>]Anda gagal dalam mata kuliah tersebut!")

    print(65*"=")
    nilai = int(input("[>]Masukkan Nilai Akhir(angka) : "))

    if 56 <= nilai <= 100 :
        if nilai >=80 :
            print("[>]Anda lulus dalam mata kuliah tersebut dengan predikat 'A'")
        elif nilai >=68 :
            print("[>]Anda lulus dalam mata kuliah tersebut dengan predikat 'B'")
        elif nilai >=56 :
            print("[>]Anda lulus dalam mata kuliah tersebut dengan predikat 'C'")

    else :
        if nilai > 100 :
            print("[>]Nilai yang anda masukkan salah!")
        elif nilai >= 40 :
            print("[>]Anda gagal dalam mata kuliah tersebut dengan predikat 'D'")

        elif nilai >= 0 :
            print("[>]Anda gagal dalam mata kuliah tersebut dengan predikat 'D'")

    print(65*"=")
    daftar = ['Rangga', 'Fasya', 'Agung', 'Andre', 'Alip', 'Daffa', 'Nisa']



    print(65*"=")
    loop = input("Ingin mengulang kembali program?(y/t) : ")
    print(5*"\n")