class faktorial :

    def __init__(self):
        self.angka = int()

    def hitung(self):
        keluar='yes'
        while (keluar=='yes') or (keluar=='YES'):
            print(50 * "*")

            try:
                self.angka=eval(input("Masukkan Angka\t\t\t: "))

                if(self.angka<=0):
                    raise ValueError

                assert ((self.angka%1)==0)

            except EOFError :
                print("\nMasukkan Input terlebih dahulu")

            except SyntaxError :
                print("\nMasukkan Input Sesuai Perintah!")

            except NameError :
                print("\nMasukkan Input berupa angka:")

            except ValueError :
                print("\nNilai angka faktorial\n tidak boleh Kurang dari sama dengan nol")

            except AssertionError :
                print("\nNilai angka faktorial\n tidak boleh berupa float(koma)")

            else :
                self.hasil = self.angka
                for i in reversed(range(1, self.angka)) :
                    self.hasil *= i
                print("\nFaktorial {} adalah\t\t: {}".format(self.angka,self.hasil))

                print(50 * "*")
                keluar = input("Apakah ingin mengulang kembali?(yes/no): ")
                print("\n")

print(50 * "*")
print("{:^50}".format("Perhitungan Faktorial"))
print((50 * "#") + "\n")

angka = faktorial()
angka.hitung()

print(50 * "#")