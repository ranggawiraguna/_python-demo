class aritmatika :

    def __init__(self,a,b):
        self.nilai1 = a
        self.nilai2 = b

    def tambah(self):
        hasil = self.nilai1 + self.nilai2
        return hasil

    def kurang(self):
        hasil = self.nilai1 - self.nilai2
        return hasil

    def kali(self):
        hasil = self.nilai1 * self.nilai2
        return hasil

    def bagi(self):
        hasil = self.nilai1 / self.nilai2
        return hasil


operasi = aritmatika(10, 10)

try :
    operasi.__delattr__("hasil")

except AttributeError as e :
    print()
    print("[!]Error Message\t\t: Pengoperasian objek menggunakan identifier gagal!")
    print("[!]Type Error\t\t\t: {}".format(str(type(e))[8:(len(str(type(e))) - 2)]))
    print("[!]Detail Error\t\t\t: Attribute '{}' tidak ditemukan!".format(e))

else :
    print()
    print("[!]Pengoperasian objek menggunakan idetifier berhasil!")

finally :
    print()
    print("[!]Blok try-except berhasil digunakan!")
