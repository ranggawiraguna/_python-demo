class tabung:

    def __init__(self):
        self.jari = float();
        self.tinggi = float();

    def hitung(self):
        keluar = 'y'
        while (keluar == 'y') or (keluar == 'Y'):
            try :
                print(50 * "-")
                pilihan = int(input("Pilihan\t\t\t\t: [1]Luas Permukaan Alas\n\t\t\t\t\t  [2]Volume Tabung\nPilih\t\t\t\t:  "))
                print(50 * "-")
                self.jari = eval(input("Masukkan Jari-Jari\t\t\t: "))
                self.tinggi = eval(input("Masukkan Tinggi Tabung\t\t: "))

                if (self.jari <= 0) or (self.tinggi <= 0):
                    raise ValueError

                assert ((self.jari % 1) == 0) and ((self.tinggi % 1) == 0)

            except EOFError:
                print("\nMasukkan Input terlebih dahulu")
                keluar = 'keluar'

            except SyntaxError:
                print("\nMasukkan Input sesuai perintah!")

            except NameError:
                print("\nMasukkan Input dengan benar!")

            except ValueError:
                print("\nNilai jari/tinggi\ntidak boleh Kurang dari sama dengan 0")

            except AssertionError:
                print("\nNilai jari/tinggi\ntidak boleh berupa float(koma)")


            else :
                if pilihan is 1:
                    self.luas = (3.14 * self.jari * self.jari)
                    print("Hasil Luas Permukaan Tabung\t:", self.luas)
                elif pilihan is 2:
                    self.volume = (3.14 * self.jari * self.jari) * self.tinggi
                    print("Hasil Volume Tabung\t\t\t:", self.volume)
                else:
                    print("Pilihan yang anda masukkan salah!")

            print(50 * "-")
            keluar = input("Apakah ingin mengulang kembali?(y/t): ")
            print("\n")

print(50 * "=")
print("{:^50}".format("MENGHITUNG LUAS/VOLUME TABUNG"))
print((50 * "=") + "\n\n")

bangunDatar = tabung()
bangunDatar.hitung()

print(50 * "=")