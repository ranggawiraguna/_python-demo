from math import pi as phi
from decimal import Decimal as dec

class lingkaran :

    def __init__(self):
        self.jariLingkaran = eval(input("Masukkan Jari-Jari Lingkaran\t: "))

    def hitungKelilingLingkaran(self):
        self.kelilingLingkaran = float( dec(str(phi)) * dec(str(self.jariLingkaran)) )
        print("Keliling Lingkaran\t\t\t\t: {:.2f}".format(self.kelilingLingkaran))

    def hitungLuasLingkaran(self):
        self.luasLingkaran = float( dec(str(phi)) * dec(str(self.jariLingkaran)) * dec(str(self.jariLingkaran)) )
        print("Luas Lingkaran\t\t\t\t\t: {:.2f}".format(self.luasLingkaran))

class tabung(lingkaran) : #Class tabung mengambil semua isi yang ada pada class lingkaran

    #__init pada tabung seharusnya sudah diwariskan oleh lingkaran, tetapi karena tabung memiliki tinggi
    #jadi tabung mempunyai attribut baru untuk tinggi, dalam hal ini dibuat lagi __init__ pada tabung sehingga __init__ yang diberikan
    #oleh lingkaran akan tertimpa(overridden)
    def __init__(self):
        self.jariLingkaran = eval(input("Masukkan Jari-Jari Lingkaran\t: "))
        self.tinggiTabung = eval(input("Masukkan Tinggi Tabung\t\t\t: "))

    def hitungVolumeTabung(self):
        self.hitungLuasLingkaran()
        print("Tinggi Tabung\t\t\t\t\t:", self.tinggiTabung)
        self.volumeTabung = float( dec(str(self.luasLingkaran)) * dec(str(self.tinggiTabung)) )
        print("Volume Tabung\t\t\t\t\t: {:.2f}".format(self.volumeTabung))

    def hitungLuasPermukaan(self):
        self.hitungLuasLingkaran()
        self.hitungKelilingLingkaran()
        print("Tinggi Tabung\t\t\t\t\t:", self.tinggiTabung)
        self.luasSelimut = float( dec(str(self.kelilingLingkaran)) * dec(str(self.tinggiTabung)) )
        print("Luas Selimut Tabung\t\t\t\t: {:.2f}".format(self.luasSelimut))
        self.luasPermukaan = float( (2 * dec(str(self.luasLingkaran))) + dec(str(self.luasSelimut)) )
        print("Luas Permukaan Tabung\t\t\t: {:.2f}".format(self.luasPermukaan))

print(50 * "=")
bangunDatar1 = lingkaran()
print()
bangunDatar1.hitungKelilingLingkaran()
print()
bangunDatar1.hitungLuasLingkaran()

print(50 * "=")
bangunDatar2 = tabung()
print()
bangunDatar2.hitungVolumeTabung()
print()
bangunDatar2.hitungLuasPermukaan()

print(50 * "=")