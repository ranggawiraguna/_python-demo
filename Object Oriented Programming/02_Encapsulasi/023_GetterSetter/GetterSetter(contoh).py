class mahasiswa :
    #Variable Private, hanya bisa diakses pada statement di dalam class saja
    #artinya, statement yang berada diluar class tidak dapat mengaksesnya

    __universitas = "Universitas Muhammadiyah Prof. Dr.Hamka"
    __fakultas = "Teknik Informatika"
    __nilaiMinMahasiswa = 56    #Private class attribut
    __nilaiMaxMahasiswa = 100   #Private class attribut
    __jumlahMahasiswa = 0


    #Method-1 pada class mahasiswa, __init__ berfungsi sebagai konstruktor atau pembbuat object yang otomatis dijalankan pada saat
    #membuat object dari class mahasiswa
    def __init__(self):
        self.__nim = input("Masukkan NIM Mahasiswa  : ")  #Private object attribut
        self.__nama = input("Masukkan Nama Mahasiswa : ") #Private object attribut
        self.__nilaiAkhir = float(input("Masukkan Nilai Akhir    : ")) #Private object attribut


    #Decorator untuk membuat sebuah method menjadi suatu attribut
    @property
    def info(self):
        return "[>]NIM         : {}\n[>]Nama        : {}\n[>]Nilai Akhir : {}".\
                format(self.__nim, self.__nama, self.__nilaiAkhir)

    @property
    def nim(self):
        pass

    @property
    def nama(self):
        pass

    @property
    def nilaiAkhir(self) :
        pass


    #Method Getter(self) dengan property
    #Decorator untuk membuat merthod menjadi suatu atribut yang berfungsi menghasilkan nilai dari attribut private
    #Hanya berlaku pada objek karena didalam method terdapat argumen self(suatu objek)
    @nim.getter
    def nim(self) :
        return self.__nim

    @nama.getter
    def nama(self) :
        return self.__nama

    @nilaiAkhir.getter
    def nilaiAkhir(self) :
        return self.__nilaiAkhir


    #Method Setter(self) dengan property
    #Decorator untuk membuat merthod menjadi suatu atribut yang berfungsi untuk mengubah nilai dari attribut private
    #Hanya berlaku pada objek karena didalam method terdapat argumen self(suatu objek)
    @nim.setter
    def nim(self, input) :
        self.__nim = input  #Private object attribut

    @nama.setter
    def nama(self,input) :
        self.__nama = input #Private object attribut

    @nilaiAkhir.setter
    def nilaiAkhir(self,input) :
        self.__nilaiAkhir = input   #Private object attribut


    # Method Deleter(self) dengan property
    # Decorator untuk membuat merthod menjadi suatu atribut yang berfungsi untuk menghapus(None) nilai dari attribut private
    # Hanya berlaku pada objek karena didalam method terdapat argumen self(suatu objek)
    @nim.deleter
    def nim(self):
        self.__nim = None  # Private object attribut

    @nama.deleter
    def nama(self):
        self.__nama = None  # Private object attribut

    @nilaiAkhir.deleter
    def nilaiAkhir(self):
        self.__nilaiAkhir = None  # Private object attribut



if __name__ == '__main__':
    print(80*"=")
    mahasiswa1 = mahasiswa()
    print()
    print(mahasiswa1.info)

    print(80*"=")
    print(mahasiswa1.nim, end=' || ')
    print(mahasiswa1.nama, end=' || ')
    print(mahasiswa1.nilaiAkhir, end=' || ')
    print("\n")
    print(mahasiswa1.info)

    print(80*"=")
    mahasiswa1.nim = input("Masukkan NIM Mahasiswa  : ")  # Private object attribut
    mahasiswa1.nama = input("Masukkan Nama Mahasiswa : ")  # Private object attribut
    mahasiswa1.nilaiAkhir = float(input("Masukkan Nilai Akhir    : "))  # Private object attribut
    print()
    print(mahasiswa1.info)

    print(80*"=")
    print("Proses Deleter Property")
    del mahasiswa1.nim
    del mahasiswa1.nama
    del mahasiswa1.nilaiAkhir
    print()
    print(mahasiswa1.info)

    print(80*"=")
