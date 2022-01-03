class mahasiswa :

    #Variable Private, hanya bisa diakses pada statement di dalam class saja
    #artinya, statement yang berada diluar class tidak dapat mengaksesnya
    __nilaiMinMahasiswa = 56    #Private class attribut
    __nilaiMaxMahasiswa = 100   #Private class attribut

    #Method-1 pada class mahasiswa, __init__ berfungsi sebagai konstruktor atau pembbuat object yang otomatis dijalankan pada saat
    #membuat object dari class mahasiswa
    def __init__(self):
        self.nim = input("Masukkan NIM Mahasiswa  : ")  #Public object attribut //dapat diakses pada statement diluar class
        self.nama = input("Masukkan Nama Mahasiswa : ") #Public object attribut //dapat diakses pada statement diluar class
        self.__totalNilai = 0   #Private object attribut

    #Method-2 pada class mahasiswa
    def inputNilai(self):
        self.__totalNilai += float(input("Masukkan Absen(%)      : ")) #Mengakses private object attribut pada statement didalam class
        self.__totalNilai += float(input("Masukkan Nilai Tugas   : ")) #Mengakses private object attribut pada statement didalam class
        self.__totalNilai += float(input("Masukkan Nilai UTS     : ")) #Mengakses private object attribut pada statement didalam class
        self.__totalNilai += float(input("Masukkan Nilai UAS     : ")) #Mengakses private object attribut pada statement didalam class

    #Method-3 pada class mahasiswa
    def cekStatus(self, nama):
        print("Nilai :", self.__totalNilai) #Mengakses private object attribut pada statement didalam class

        if self.__totalNilai < mahasiswa.__nilaiMinMahasiswa : #Mengakses private object attribut pada statement didalam class
            print("[!]Mahasiswa {} tidak lulus".format(nama))

        elif self.__totalNilai < mahasiswa.__nilaiMaxMahasiswa : #Mengakses private object attribut pada statement didalam class
            print("[!]Mahasiswa {} lulus".format(nama))

        elif self.__totalNilai > mahasiswa.__nilaiMaxMahasiswa : #Mengakses private object attribut pada statement didalam class
            print("[!]Terdapat kesalah pada inputNilai")


#Menggunakan Method melalui object mahasiswa1 yang telah ditetapkan sebagai object dari class mahasiswa
print(50*"=")
mahasiswa1 = mahasiswa()    #Pembuatan object otamtis akan menjalan fungsi __init__ yang ada didalam class
print()
mahasiswa1.inputNilai()
print()
print("[>]NIM   :", mahasiswa1.nim)      #Mengakses public attribut dari mahasiswa1
print("[>]Nama  :", mahasiswa1.nama)     #Mengakses public attribut dari mahasiswa1
mahasiswa1.cekStatus(mahasiswa1.nama)   #Mengakses public attribut dari mahasiswa1
print()
mahasiswa1.nim = input("Masukkan NIM Mahasiswa  : ")  #Public object attribut //dapat diakses pada statement diluar class
mahasiswa1.nama = input("Masukkan Nama Mahasiswa : ")  # Public object attribut //dapat diakses pada statement diluar class


#Menggunakan Method melalui object mahasiswa2 yang telah ditetapkan sebagai object dari class mahasiswa
print(50*"=")
mahasiswa2 = mahasiswa()    #Pembuatan object otamtis akan menjalan fungsi __init__ yang ada didalam class
print()
mahasiswa2.inputNilai()
print()
print("[>]NIM   :", mahasiswa2.nim)      #Mengakses public attribut dari mahasiswa2
print("[>]Nama  :", mahasiswa2.nama)     #Mengakses public attribut dari mahasiswa2
mahasiswa2.cekStatus(mahasiswa2.nama)   #Mengakses public attribut dari mahasiswa2
print()
mahasiswa2.nim = input("Masukkan NIM Mahasiswa  : ")  #Public object attribut //dapat diakses pada statement diluar class
mahasiswa2.nama = input("Masukkan Nama Mahasiswa : ")  # Public object attribut //dapat diakses pada statement diluar class

print(50*"=")
