class layang:

    def __init__(self):
        self.d1 = float()
        self.d2 = float()
        self.a = float()
        self.b = float()
        self.c = float()
        self.d = float()

    def hitung(self):
        keluar = 'y'
        while (keluar == 'y') or (keluar == 'Y'):
            try :
                print(50 * "-")
                pilihan = int(input("Pilihan\t\t\t\t: [1]Luas\n\t\t\t\t\t  [2]Keliling\nPilih\t\t\t\t:  "))
                print(50 * "-")

                if pilihan is 1:
                    self.d1 = eval(input("Masukkan Diagonal-1\t: "))
                    self.d2 = eval(input("Masukkan Diagonal-2\t: "))

                    if (self.d1 <= 0) or (self.d2 <= 0):
                        raise ValueError

                    assert ((self.d1 % 1) == 0) and ((self.d2 % 1) == 0)

                    self.hasil = (0.5)*(self.d1 * self.d2)

                elif pilihan is 2:
                    self.a = eval(input("Masukkan Sisi (a)\t\t: "))
                    self.b = eval(input("Masukkan Sisi (b)\t\t: "))
                    self.c = eval(input("Masukkan Sisi (c)\t\t: "))
                    self.d = eval(input("Masukkan Sisi (d)\t\t: "))

                    if (self.a <= 0) or (self.b <= 0) or (self.c <= 0) or (self.d <= 0):
                        raise ValueError

                    assert ((self.a % 1) == 0) and ((self.b % 1) == 0) and ((self.c % 1) == 0) and ((self.d % 1) == 0)

                    self.hasil = (self.a + self.b + self.c + self.d)

                else:
                    print("Pilihan yang anda masukkan salah!")

            except EOFError:
                print("\nMasukkan Input terlebih dahulu")
                keluar = 'keluar'

            except SyntaxError:
                print("\nMasukkan Input sesuai perintah!")

            except NameError:
                print("\nMasukkan Input dengan benar!")

            except ValueError:
                print("\nNilai yang dimasukkan\ntidak boleh Kurang dari sama dengan nol")

            except AssertionError:
                print("\nNilai yang dimasukkan\ntidak boleh berupa float(koma)")

            else :
                if pilihan is 1 :
                    print("Hasil Luas\t\t\t:", self.hasil)
                elif pilihan is 2 :
                    print("Hasil Keliling\t\t\t:", self.hasil)

                print(50 * "-")
                keluar = input("Apakah ingin mengulang kembali?(y/t): ")
                print("\n")

print(50 * "=")
print("{:^50}".format("MENGHITUNG LUAS/KELILING LAYANG-LAYANG"))
print((50 * "=") + "\n\n")

bangunDatar = layang()
bangunDatar.hitung()

print(50 * "=")