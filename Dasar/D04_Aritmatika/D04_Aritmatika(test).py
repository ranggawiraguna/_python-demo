#ARITMATIKA

import os #Import object os

print("==================================================")
print("Selamat Datang\n") #print() >> otomatis enter

print("Masukkan Biodata User")       #print() >> otomatis enter
print("[>]Masukkan Nama : ")        #print() >> otomatis enter
nama = input()                       #input() >> otomatis menyimpan data string
nim =  input("[>]Masukkan NIM  : ")  #input("Teks") >> otomatis menyimpan data string dan menampilkan teks sebelum perintah input
print("==================================================\n\n\n")

while True :
    os.system('cls')    #>perintah clearscreen yang berasal dari object os di field system

    print("\n==================================================")
    print("BIODATA USER : " + nama + "(" + nim + ")" ) #print() dengan concat(+) hanya dapat menampilkan data string didalamnya
    print("==================================================")

    print("Pilihan\t: [1]Penambahan\n\t\t  [2]Pengurangan\n\t\t  [3]Perkalian\n\t\t  [4]Pembagian\n\t\t  [5]Pangkat\n\t\t  [6]Divisi\n\t\t  [7]modulus\n\t\t  [0]Keluar")
    pilihan = input("Pilihan\t:  ")
    print()

    if pilihan is '0' :
        print("==================================================")
        exit();

    elif pilihan is '1' :
        print("PENAMBAHAN")
        a = int(input("[>]Masukkan Nilai-1\t\t: "))                     #type(input()) >> untuk non string  >> menentukan tipedata dari data yang akan disimpan pada variable
        b = int(input("[>}Masukkan Nilai-2\t\t: "))                     #type(input()) >> untuk non string  >> menentukan tipedata dari data yang akan disimpan pada variable
        c =  a + b;                                                     #var c bernilai float karena penambahan antara kedua nilai numerik(menyesuaikan)
        print("[>]Hasil dari " + str(a) + " + " + str(b) + " \t: " + str(c))   #print() dengan concat '+', khusus tipedata selain string harus mengcasting var ke tipedata string >> str(var)
        print("[>]Hasil dari", a, "+", b, "\t:", c)                            #print() yang menambahkan objek lain dengan ',' otomatis memberikan spasi diantara pemisah ',' nya dan akan mengcasting otomatis variable selain string

    elif pilihan is '2' :
        print("PENGURANGAN")
        a = int(input("[>]Masukkan Nilai-1\t\t: "))                     #type(input()) >> untuk non string  >> menentukan tipedata dari data yang akan disimpan pada variable
        b = int(input("[>}Masukkan Nilai-2\t\t: "))                     #type(input()) >> untuk non string  >> menentukan tipedata dari data yang akan disimpan pada variable
        c =  a - b;                                                     #var c bernilai float karena penambahan antara kedua nilai numerik(menyesuaikan)
        print("[>]Hasil dari " + str(a) + " - " + str(b) + " \t: " + str(c))   #print() dengan concat '+', khusus tipedata selain string harus mengcasting var ke tipedata string >> str(var)
        print("[>]Hasil dari", a, "-", b, "\t:", c)                            #print() yang menambahkan objek lain dengan ',' otomatis memberikan spasi diantara pemisah ',' nya dan akan mengcasting otomatis variable selain string

    elif pilihan is '3' :
        print("PERKALIAN")
        a = int(input("[>]Masukkan Nilai-1\t\t: "))                     #type(input()) >> untuk non string  >> menentukan tipedata dari data yang akan disimpan pada variable
        b = int(input("[>}Masukkan Nilai-2\t\t: "))                     #type(input()) >> untuk non string  >> menentukan tipedata dari data yang akan disimpan pada variable
        c =  a * b;                                                     #var c bernilai float karena penambahan antara kedua nilai numerik(menyesuaikan)
        print("[>]Hasil dari " + str(a) + " x " + str(b) + " \t: " + str(c))   #print() dengan concat '+', khusus tipedata selain string harus mengcasting var ke tipedata string >> str(var)
        print("[>]Hasil dari", a, "x", b, "\t:", c)                            #print() yang menambahkan objek lain dengan ',' otomatis memberikan spasi diantara pemisah ',' nya dan akan mengcasting otomatis variable selain string

    elif pilihan is '4' :
        print("PEMBAGIAN")
        a = float(input("[>]Masukkan Nilai-1\t\t\t: "))                     #type(input()) >> untuk non string  >> menentukan tipedata dari data yang akan disimpan pada variable
        b = float(input("[>}Masukkan Nilai-2\t\t\t: "))                     #type(input()) >> untuk non string  >> menentukan tipedata dari data yang akan disimpan pada variable
        c =  a / b;                                                     #var c bernilai float karena penambahan antara kedua nilai numerik(menyesuaikan)
        print("[>]Hasil dari " + str(a) + " / " + str(b) + " \t: " + str(c))   #print() dengan concat '+', khusus tipedata selain string harus mengcasting var ke tipedata string >> str(var)
        print("[>]Hasil dari", a, "/", b, "\t:", c)                            #print() yang menambahkan objek lain dengan ',' otomatis memberikan spasi diantara pemisah ',' nya dan akan mengcasting otomatis variable selain string

    elif pilihan is '5' :
        print("PANGKAT")
        a = int(input("[>]Masukkan Nilai-1\t\t: "))                     #type(input()) >> untuk non string  >> menentukan tipedata dari data yang akan disimpan pada variable
        b = int(input("[>}Masukkan Nilai-2\t\t: "))                     #type(input()) >> untuk non string  >> menentukan tipedata dari data yang akan disimpan pada variable
        c =  a ** b;                                                     #var c bernilai float karena penambahan antara kedua nilai numerik(menyesuaikan)
        print("[>]Hasil dari " + str(a) + " ** " + str(b) + " \t: " + str(c))   #print() dengan concat '+', khusus tipedata selain string harus mengcasting var ke tipedata string >> str(var)
        print("[>]Hasil dari", a, "**", b, "\t:", c)                            #print() yang menambahkan objek lain dengan ',' otomatis memberikan spasi diantara pemisah ',' nya dan akan mengcasting otomatis variable selain string

    elif pilihan is '6' :
        print("DIVISI")
        a = int(input("[>]Masukkan Nilai-1\t\t: "))                     #type(input()) >> untuk non string  >> menentukan tipedata dari data yang akan disimpan pada variable
        b = int(input("[>}Masukkan Nilai-2\t\t: "))                     #type(input()) >> untuk non string  >> menentukan tipedata dari data yang akan disimpan pada variable
        c =  a // b;                                                     #var c bernilai float karena penambahan antara kedua nilai numerik(menyesuaikan)
        print("[>]Hasil dari " + str(a) + " // " + str(b) + " \t: " + str(c))   #print() dengan concat '+', khusus tipedata selain string harus mengcasting var ke tipedata string >> str(var)
        print("[>]Hasil dari", a, "//", b, "\t:", c)                            #print() yang menambahkan objek lain dengan ',' otomatis memberikan spasi diantara pemisah ',' nya dan akan mengcasting otomatis variable selain string

    elif pilihan is '7' :
        print("MODULUS")
        a = int(input("[>]Masukkan Nilai-1\t\t: "))                     #type(input()) >> untuk non string  >> menentukan tipedata dari data yang akan disimpan pada variable
        b = int(input("[>}Masukkan Nilai-2\t\t: "))                     #type(input()) >> untuk non string  >> menentukan tipedata dari data yang akan disimpan pada variable
        c =  a % b;                                                     #var c bernilai float karena penambahan antara kedua nilai numerik(menyesuaikan)
        print("[>]Hasil dari " + str(a) + " % " + str(b) + " \t: " + str(c))   #print() dengan concat '+', khusus tipedata selain string harus mengcasting var ke tipedata string >> str(var)
        print("[>]Hasil dari", a, "%", b, "\t:", c)                            #print() yang menambahkan objek lain dengan ',' otomatis memberikan spasi diantara pemisah ',' nya dan akan mengcasting otomatis variable selain string

    else :
        print("Note\t: [*]Pilihan yang Anda masukkan salah!")

    print("==================================================\n\n")
