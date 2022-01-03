class mahasiswa :

    #Variable Private, hanya bisa diakses pada statement di dalam class saja
    #artinya, statement yang berada diluar class tidak dapat mengaksesnya
    __nilaiMinMahasiswa = 56    #Private class attribut
    __nilaiMaxMahasiswa = 100   #Private class attribut

    #Method-1 pada class mahasiswa, __init__ berfungsi sebagai konstruktor atau pembbuat object yang otomatis dijalankan pada saat
    #membuat object dari class mahasiswa
    def __init__(self):
        self.nim = input("Masukkan NIM Mahasiswa  : ")
        self.nama = input("Masukkan Nama Mahasiswa : ")
        self.__totalNilai = 0   #Private object attribut

    #Method-2 pada class mahasiswa
    def inputNilai(self):
        self.__totalNilai += float(input("Masukkan Absen(%)      : "))
        self.__totalNilai += float(input("Masukkan Nilai Tugas   : "))
        self.__totalNilai += float(input("Masukkan Nilai UTS     : "))
        self.__totalNilai += float(input("Masukkan Nilai UAS     : "))

    #Method-3 pada class mahasiswa
    def cekStatus(self, nama):
        print("Total Nilai Mahasiswa  :", self.__totalNilai)

        if self.__totalNilai < mahasiswa.__nilaiMinMahasiswa :
            print("[!]Mahasiswa {} tidak lulus".format(nama))

        elif self.__totalNilai < mahasiswa.__nilaiMaxMahasiswa :
            print("[!]Mahasiswa {} lulus".format(nama))

        elif self.__totalNilai > mahasiswa.__nilaiMaxMahasiswa :
            print("[!]Terdapat kesalah pada inputNilai")


#Menggunakan Method melalui object mahasiswa1 yang telah ditetapkan sebagai object dari class mahasiswa
print(50*"=")
mahasiswa1 = mahasiswa()    #Pembuatan object otamtis akan menjalan fungsi __init__ yang ada didalam class
mahasiswa1.inputNilai()
mahasiswa1.cekStatus(mahasiswa1.nama)

#Menggunakan Method melalui object mahasiswa2 yang telah ditetapkan sebagai object dari class mahasiswa
print(50*"=")
mahasiswa2 = mahasiswa()    #Pembuatan object otamtis akan menjalan fungsi __init__ yang ada didalam class
mahasiswa2.inputNilai()
mahasiswa2.cekStatus(mahasiswa2.nama)

print(50*"=")
