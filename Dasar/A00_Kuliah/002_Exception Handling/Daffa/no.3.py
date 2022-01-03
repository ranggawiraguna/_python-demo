class kubus:

    def __init__(self):
        self.sisi = float();

    def hitung(self):
        keluar = 'y'
        while (keluar == 'y') or (keluar == 'Y'):
            try :

                print(50 * "-")
                pilihan = int(input("Pilihan\t\t\t\t: [1]Luas Seluruh Permukaan\n\t\t\t\t\t  [2]Volume Kubus\nPilih\t\t\t\t:  "))
                print(50 * "-")
                self.sisi = eval(input("Masukkan Sisi\t\t\t\t\t: "))

                if (self.sisi <= 0):
                    raise ValueError

                assert ((self.sisi % 1) == 0)

            except EOFError:
                print("\nMasukkan Input terlebih dahulu")

            except SyntaxError:
                print("\nMasukkan Input sesuai perintah!")

            except NameError:
                print("\nMasukkan Input berupa angka!")

            except ValueError:
                print("\nNilai sisi\ntidak boleh Kurang dari sama dengan nol")

            except AssertionError:
                print("\nNilai sisi\ntidak boleh berupa float(koma)")

            else :
                if pilihan is 1:
                    self.luas = ((self.sisi * self.sisi) * 6)
                    print("Hasil Luas Seluruh Permukaan\t:", self.luas)
                elif pilihan is 2:
                    self.volume = (self.sisi * self.sisi * self.sisi)
                    print("Hasil Volume Kubus\t\t\t\t:", self.volume)
                else:
                    print("Pilihan yang anda masukkan salah!")

            print(50 * "-")
            keluar = input("Apakah ingin mengulang kembali?(y/t): ")
            print("\n")


print(50 * "=")
print("{:^50}".format("MENGHITUNG LUAS/VOLUME KUBUS"))
print((50 * "=") + "\n")

bangunDatar = kubus()
bangunDatar.hitung()

print(50 * "=")


