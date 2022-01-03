class balok :
        def __init__(self):
            self.panjang = float();
            self.lebar = float();
            self.tinggi = float();

        def hitung(self):
            keluar = 'y'
            while (keluar == 'y') or (keluar=='Y') :
                print(50 * "-")
                try :
                    print(50 * "-")
                    pilihan = int(input("Pilihan\t\t\t\t: [1]Luas Seluruh Permukaan\n\t\t\t\t\t  [2]Volume\nPilih\t\t\t\t:  "))
                    print(50 * "-")
                    self.panjang = eval(input("Masukkan Panjang\t\t\t\t: "))
                    self.lebar = eval(input("Masukkan Lebar\t\t\t\t\t: "))
                    self.tinggi = eval(input("Masukkan Tinggi\t\t\t\t\t: "))
                    if (self.panjang <= 0) or (self.lebar <= 0) or (self.tinggi <= 0):
                        raise ValueError
                    assert ((self.panjang % 1) == 0) and ((self.lebar % 1) == 0) and ((self.tinggi % 1) == 0)
                except EOFError:
                    print("\nMasukkan Input terlebih dahulu")
                    keluar = 'keluar'
                except SyntaxError:
                    print("\nMasukkan Input sesuai perintah!")
                except NameError:
                    print("\nMasukkan Input dengan benar!")
                except ValueError:
                    print("\nBatas panjang/lebar/tinggi\ntidak boleh Kurang dari sama dengan 0")
                except AssertionError:
                    print("\nNilai panjang/lebar/tinggi\ntidak boleh berupa float(koma)")
                else :
                    if pilihan is 1 :
                        self.luas = ((self.lebar * self.tinggi)*2) + ((self.panjang * self.lebar)*2) + ((self.panjang * self.tinggi)*2)
                        print("Hasil Luas Seluruh Permukaan\t:", self.luas)
                    elif pilihan is 2:
                        self.volume = (self.panjang * self.lebar * self.tinggi)
                        print("Hasil Volume\t\t\t\t\t:", self.volume)
                    else :
                        print("Pilihan yang anda masukkan salah!")

                    print(50 * "-")
                    keluar = input("Apakah ingin mengulang kembali?(y/t): ")
                    print("\n")

print(50 * "=")
print("{:^50}".format("MENGHITUNG LUAS/VOLUME BALOK"))
print((50 * "=") + "\n")
bangunDatar = balok();
bangunDatar.hitung()
print(50 * "=")


