class persegiPanjang:

    def __init__(self):
        self.panjang = float();
        self.lebar = float();

    def hitung(self):
        keluar = 'y'
        while (keluar == 'y') or (keluar == 'Y'):
            try :
                print(50 * "-")
                pilihan = int(input("Pilihan\t\t\t\t: [1]Luas\n\t\t\t\t\t  [2]Keliling\nPilih\t\t\t\t:  "))
                print(50 * "-")
                self.panjang = eval(input("Masukkan Panjang\t\t\t\t: "))
                self.lebar = eval(input("Masukkan Lebar\t\t\t\t\t: "))

                if (self.panjang <= 0) or (self.lebar <= 0):
                    raise ValueError

                assert ((self.panjang % 1) == 0) and ((self.lebar % 1) == 0)

            except EOFError:
                print("\nMasukkan Input terlebih dahulu")
                keluar = 'keluar'

            except SyntaxError:
                print("\nMasukkan Input sesuai perintah!")

            except NameError:
                print("\nMasukkan Input dengan benar!")

            except ValueError:
                print("\nNilai panjang/lebar\ntidak boleh Kurang dari sama dengan 0")

            except AssertionError:
                print("\nNilai panjang/lebar\ntidak boleh berupa float(koma)")

            else :
                if pilihan is 1:
                    self.luas = (self.lebar * self.panjang)
                    print("Hasil Luas Persegi Panjang\t:", self.luas)
                elif pilihan is 2:
                    self.keliling = (self.panjang + self.lebar) * 2
                    print("Hasil Keliling\t\t\t\t\t:", self.keliling)
                else:
                    print("Pilihan yang anda masukkan salah!")
                print(50 * "-")
                keluar = input("Apakah ingin mengulang kembali?(y/t): ")
                print("\n")


print(50 * "=")
print("{:^50}".format("MENGHITUNG LUAS/KELILING PERSEGI PANJANG"))
print((50 * "=") + "\n")
bangunDatar = persegiPanjang();
bangunDatar.hitung()
print(50 * "=")