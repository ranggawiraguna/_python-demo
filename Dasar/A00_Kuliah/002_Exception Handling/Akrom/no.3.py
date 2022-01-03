class persegi:

    def __init__(self):
        self.sisi = float()

    def hitung(self):
        keluar = 'y'
        while (keluar == 'y') or (keluar == 'Y'):
            try :
                print(50 * "-")
                pilihan = int(input("Pilihan\t\t\t\t: [1]Luas\n\t\t\t\t\t  [2]Keliling\nPilih\t\t\t\t:  "))
                print(50 * "-")
                self.sisi = eval(input("Masukkan sisi\t\t: "))

                if (self.sisi <= 0):
                    raise ValueError

                assert ((self.sisi%1)==0)

            except EOFError:
                print("\nMasukkan Input terlebih dahulu")

            except SyntaxError:
                print("\nMasukkan Input sesuai perintah!")

            except NameError:
                print("\nMasukkan Input dengan benar!")

            except ValueError:
                print("\nNilai sisi\ntidak boleh Kurang dari sama dengan 0")

            except AssertionError:
                print("\nNilai sisi\ntidak boleh berupa float(koma)")

            else :
                if pilihan is 1:
                    self.luas = (self.sisi * self.sisi)
                    print("Hasil Luas Persegi\t:", self.luas)
                elif pilihan is 2:
                    self.keliling = (self.sisi * 4)
                    print("Hasil Keliling\t\t\t\t\t:", self.keliling)
                else:
                    print("Pilihan yang anda masukkan salah!")

            print(50 * "-")
            keluar = input("Apakah ingin mengulang kembali?(y/t): ")
            print("\n")


print(50 * "=")
print("{:^50}".format("MENGHITUNG LUAS/KELILING PERSEGI"))
print((50 * "=") + "\n")
bangunDatar = persegi()
bangunDatar.hitung()
print(50 * "=")


