#Encapsulasi //Membuat semua attribut pada class bersifat private, artinya attribut tidak dapat diakses pada perintah diluar class

class mahasiswa :
    #Variable Private, hanya bisa diakses pada statement di dalam class saja
    #artinya, statement yang berada diluar class tidak dapat mengaksesnya
    __nilaiMinMahasiswa = 56    #Private class attribut
    __nilaiMaxMahasiswa = 100   #Private class attribut

    #Method-1 pada class mahasiswa, __init__ berfungsi sebagai konstruktor atau pembbuat object yang otomatis dijalankan pada saat
    #membuat object dari class mahasiswa
    def __init__(self):
        self.__nim = input("Masukkan NIM Mahasiswa  : ")  #Private object attribut
        self.__nama = input("Masukkan Nama Mahasiswa : ") #Private object attribut
        self.__totalNilai = 0   #Private object attribut

    #Method-2 pada class mahasiswa
    def inputNilai(self):
        self.__totalNilai += float(input("Masukkan Absen(%)      : ")) #Mengakses private object attribut pada statement didalam class
        self.__totalNilai += float(input("Masukkan Nilai Tugas   : ")) #Mengakses private object attribut pada statement didalam class
        self.__totalNilai += float(input("Masukkan Nilai UTS     : ")) #Mengakses private object attribut pada statement didalam class
        self.__totalNilai += float(input("Masukkan Nilai UAS     : ")) #Mengakses private object attribut pada statement didalam class

    #Method-3 pada class mahasiswa
    def cekStatus(self):

        if self.__totalNilai < mahasiswa.__nilaiMinMahasiswa : #Mengakses private object attribut pada statement didalam class
            print("[!]Mahasiswa {} tidak lulus".format(self.__nama))

        elif self.__totalNilai < mahasiswa.__nilaiMaxMahasiswa : #Mengakses private object attribut pada statement didalam class
            print("[!]Mahasiswa {} lulus".format(self.__nama))

        elif self.__totalNilai > mahasiswa.__nilaiMaxMahasiswa : #Mengakses private object attribut pada statement didalam class
            print("[!]Terdapat kesalah pada inputNilai")

    #Method Getter //Mengakses private attribut dari dalam class dengan menggunakan method
    def getNim(self) :
        return self.__nim

    def getNama(self) :
        return self.__nama

    def getTotalNilai(self) :
        return self.__totalNilai

    #Method Setter //Mengakses private attribut dari dalam class dengan menggunakan method
    def setNim(self) :
        self.__nim = input("Masukkan NIM Mahasiswa  : ")    #Private object attribut

    def setNama(self) :
        self.__nama = ("Masukkan Nama Mahasiswa : ")        #Private object attribut


#Menggunakan Method melalui object mahasiswa1 yang telah ditetapkan sebagai object dari class mahasiswa
print(50*"=")
mahasiswa1 = mahasiswa()    #Pembuatan object otamtis akan menjalan fungsi __init__ yang ada didalam class
print()
mahasiswa1.inputNilai()
print()
#print("[>]NIM  :", mahasiswa1.__nim)       #Tidak dapat mengakses private attribut dari mahasiswa1
#print("[>]Nama :", mahasiswa1.__nama)      #Tidak dapat mengakses private attribut dari mahasiswa1
print("[>]NIM   :", mahasiswa1.getNim())    #Mengakses attribut dengan method getter
print("[>]Nama  :", mahasiswa1.getNama())   #Mengakses attribut dengan method getter
print("[>]Nilai :", mahasiswa1.getTotalNilai()) #Mengakses attribut dengan method getter
mahasiswa1.cekStatus()                         #Mengakses attribut dengan method getter
print()
mahasiswa1.setNim()     #Mengakses attribut dengan method setter
mahasiswa1.setNama()    #Mengakses attribut dengan method setter

#Menggunakan Method melalui object mahasiswa2 yang telah ditetapkan sebagai object dari class mahasiswa
print(50*"=")
mahasiswa2 = mahasiswa()    #Pembuatan object otamtis akan menjalan fungsi __init__ yang ada didalam class
mahasiswa2.inputNilai()
#print("[>]NIM  :", mahasiswa2.__nim)      #Tidak dapat mengakses private attribut dari mahasiswa2
#print("[>]Nama :", mahasiswa2.__nama)     #Tidak dapat mengakses private attribut dari mahasiswa2
print("[>]NIM   :", mahasiswa2.getNim())
print("[>]Nama  :", mahasiswa2.getNama())
print("[>]Nilai :", mahasiswa2.getTotalNilai())
mahasiswa2.cekStatus()                         #Mengakses public attribut dari mahasiswa2
print()
mahasiswa2.setNim()     #Mengakses attribut dengan method setter
mahasiswa2.setNama()    #Mengakses attribut dengan method setter

print(50*"=")

