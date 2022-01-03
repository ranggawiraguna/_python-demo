import os

data = []
pilihan = ' '

while pilihan is not '0' :
    os.system('cls')
    print(50 * "=")
    print("Pilihan\t: [1]Lihat data Mahasiswa\n\t\t  [2]Tambah data Mahasiswa\n\t\t  [3]Hapus data Mahasiswa\n\t\t  [0]Keluar")
    pilihan = input("Pilihan\t:  ")
    print(50 * "=")
    print(50 * "-")

    if pilihan is '0' :
        exit()

    elif pilihan is '1' :
        if len(data) is not 0 :
            print()
            for i in range(len(data)):
                print("Mahasiswa-" + str(i + 1))
                print("[>]Nama : " + str(data[i][0]))
                print("[>]NIM  : " + str(data[i][1]))
                print()

        else :
            print("Data Mahasiswa masih kosong!")

    elif pilihan is '2' :
        temp = []
        print("Input Data Mahasiswa")
        temp.append(input("[>]Masukkan Nama\t: "))
        temp.append(input("[>]Masukkan NIM\t\t: "))
        data.append(temp)

    elif pilihan is '3' :
        buffer = 0
        cari = 0;
        key = input("[!]Masukkan NIM data Mahasiswa yang ingin dihapus\n[>]")

        for i in range(len(data)) :
            if (data[i][1] == key) :
                cari = 1
                del data[i]
                print("[!]Data dengan NIM : " + str(data[i][1]) + " telah dihapus")
                break

        if cari is 0 :
            print("[!]Data dengan NIM yang dicari tidak ditemukan")

    else :
        print("Pilihan tidak tersedia!")

    print(50 * "-")
    print(50 * "=")
    input("Note : Tekan enter untuk melanjutkan!")
    print(3*"\n")
