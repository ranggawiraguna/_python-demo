#Fungsi didalam class dengan argumen self, menandakan bahwa method tersebut khusus untuk objek / tidak bisa digunakan oleh class
#Fungsi didalam class dengan argumen tanpa self, menandakan bahwa method tersebut khusus untuk class / tidak bisa digunakan oleh objek

#StaticMethod
#Class Method

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
        self.__nilaiAkhir = 0   #Private object attribut


    #Method-2 pada class mahasiswa
    def inputNilai(self):
        self.__nilaiAkhir += float(input("Masukkan Nilai Akhir    : ")) #Mengakses private object attribut pada statement didalam class


    #Method-3 pada class mahasiswa
    def cekStatus(self):

        if self.__nilaiAkhir < mahasiswa.__nilaiMinMahasiswa : #Mengakses private object attribut pada statement didalam class
            print("[!]Mahasiswa {} tidak lulus".format(self.__nama))

        elif self.__nilaiAkhir < mahasiswa.__nilaiMaxMahasiswa : #Mengakses private object attribut pada statement didalam class
            print("[!]Mahasiswa {} lulus".format(self.__nama))

        elif self.__nilaiAkhir > mahasiswa.__nilaiMaxMahasiswa : #Mengakses private object attribut pada statement didalam class
            print("[!]Terdapat kesalah pada inputNilai")


    #Method Getter(self)
    #Hanya berlaku pada objek karena didalam method terdapat argumen self(suatu objek)
    def getNim(self) :
        return self.__nim

    def getNama(self) :
        return self.__nama

    def getTotalNilai(self) :
        return self.__nilaiAkhir


    #Method Getter()
    #Hanya berlaku pada class, tidak berlaku pada objek
    def getJumlahMahasiswa():
        return mahasiswa.__jumlahMahasiswa

    def getRangeKelulusan():
        return (mahasiswa.__nilaiMaxMahasiswa - mahasiswa.__nilaiMinMahasiswa)


    #Method Getter() dengan decorator @classmethod
    #Berlaku pada class maupun objek, argumen didalam method dianggap sebagai objek walaupun itu sebuah class
    @classmethod
    def getUniversitas(selfClass):
        return selfClass.__universitas

    @classmethod
    def getFakultas(selfClass):
        return selfClass.__fakultas


    #Method Getter() dengan decorator @staticmethod
    #Berlaku pada class maupun objek, bisa digunakan tanpa argumen
    @staticmethod
    def getUniversitas2():
        return mahasiswa.__universitas

    @staticmethod
    def getFakultas2():
        return mahasiswa.__fakultas


if __name__ == '__main__':
    print(80*"=")
    mahasiswa1 = mahasiswa()
    mahasiswa1.inputNilai()
    print()
    mahasiswa1.cekStatus()

    print(80*"=")
    print("NIM   :", mahasiswa1.getNim())
    print("Nama  :", mahasiswa1.getNama())
    print("Nilai :", mahasiswa1.getTotalNilai())

    print(80*"=")
    print("Jumlah Mahasiswa :", mahasiswa.getJumlahMahasiswa())
    print("Range Kelulusan  :", mahasiswa.getRangeKelulusan())

    print(80*"=")
    print(mahasiswa.getUniversitas(),"||",mahasiswa.getFakultas())
    print()
    print("NIM         :", mahasiswa1.getNim())
    print("Nama        :", mahasiswa1.getNama())
    print("Nilai       :", mahasiswa1.getTotalNilai())
    print("Universitas :", mahasiswa1.getUniversitas())
    print("Fakultas    :", mahasiswa1.getFakultas())

    print(80*"=")
    print(mahasiswa.getUniversitas2())
    print(mahasiswa.getFakultas2())
    print()
    print("NIM         :", mahasiswa1.getNim())
    print("Nama        :", mahasiswa1.getNama())
    print("Nilai       :", mahasiswa1.getTotalNilai())
    print("Universitas :", mahasiswa1.getUniversitas2())
    print("Fakultas    :", mahasiswa1.getFakultas2())

    print(80*"=")
