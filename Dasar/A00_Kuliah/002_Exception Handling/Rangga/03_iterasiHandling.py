#DEKLARASI CLASS
class iterasi :

    pilihan = str()
    error = bool()

    def __init__(self, pilih):
        iterasi.pilihan = pilih

        #Pembuatan attribute dan memeriksa kesalahan pada saat input user dilakukan
        try :
            if iterasi.pilihan is '1' :
                self.angka = eval(input("[>]Masukkan Angka\t\t: "))
                self.pangkat = eval(input("[>]Masukkan Pangkat\t\t: "))

            elif iterasi.pilihan is '2' :
                self.angka = eval(input("[>]Masukkan Angka\t\t: "))

            elif iterasi.pilihan is '3' :
                self.deret = eval(input("[>]Masukkan Deret\t\t: "))

            else :
                print("[>]Pilihan yang dimasukkan salah!")

            iterasi.error = False

        #Exception handling untuk segala kemungkinan error runtime pada fungsi eval() dan input()
        except (AttributeError,SyntaxError,NameError,EOFError,KeyboardInterrupt) as e:
            print()
            print("[!]Error Message\t\t: Masukkan input dengan benar!")
            print("[!]Type Error\t\t\t: {}".format(str(type(e))[8:(len(str(type(e)))-2)]))
            print("[!]Detail Error\t\t\t: {}".format(e))
            iterasi.error = True

    def perhitungan(self):
        if iterasi.error is False :
            if iterasi.pilihan is '1' :
                try :
                    self.hasil = self.angka
                    baris = 0
                    for i in range(1,(self.pangkat)) :
                        if baris == 0 :
                            print("[>]Operasi Hitung\t\t:", self.angka, end='')
                        if ((baris % 10) == 0) and (baris != 0):
                            print(" * \n\t\t\t\t\t\t ", self.angka, end='')
                        else :
                            print(" *", self.angka, end='')
                        self.hasil *= self.angka
                        baris += 1
                    print("\n[>]Hasil Hitung\t\t\t:", self.hasil)

                except TypeError as e :
                    print()
                    print("[!]Error Message\t\t: Masukkan pangkat dengan bilangan bulat!")
                    print("   \t\t\t\t\t\t  {}".format(e))
                    print("[!]Type Error\t\t\t: {}".format(str(type(e))[8:(len(str(type(e))) - 2)]))
                    print("[!]Detail Error\t\t\t: iterasi tidak dapat menghitung Angka dengan Pangkat yang bernilai float")


            elif iterasi.pilihan is '2' :
                try :
                    self.hasil = self.angka
                    if ((self.angka%1) != 0) :
                        raise ValueError(self.angka)
                    print("[>]Operasi Hitung\t\t:", self.angka, end='')
                    baris = 0
                    for i in reversed(range(1, (self.angka))):
                        if ((baris % 10) == 0) and (baris != 0) :
                            print(" * \n\t\t\t\t\t\t ", i, end='')
                        print(" * ", i, end='')
                        self.hasil *= i
                        baris += 1
                    print("\n[>]Hasil Hitung\t\t\t:", self.hasil)

                except ValueError as e :
                    print()
                    print("[!]Error Message\t\t: Masukkan Angka dengan bilangan bulat!")
                    print("   \t\t\t\t\t\t  Factorial '{}' could not be found".format(e))
                    print("[!]Type Error\t\t\t: {}".format(str(type(e))[8:(len(str(type(e))) - 2)]))
                    print("[!]Detail Error\t\t\t: iterasi tidak dapat menghitung faktorial dari Angka yang bernilai float")

            elif iterasi.pilihan is '3' :
                try :
                    buffer1 = int(0)
                    buffer2 = int(1)
                    buffer3 = buffer1 + buffer2
                    assert (self.deret % 1) == 0, self.deret
                    print("[>]Deret Fibonacci\t\t:", buffer1, " | ", buffer2, end='')
                    for i in range(2, (self.deret+1)):
                        buffer3 = buffer1 + buffer2;
                        print(" | ", buffer3, end='')
                        buffer1 = buffer2
                        buffer2 = buffer3
                    self.hasil = buffer3
                    print("\n[>]Fibonacci ke-{}\t\t: {}".format(self.deret,self.hasil))

                except AssertionError as e :
                    print()
                    print("[!]Error Message\t\t: Masukkan Deret dengan bilangan bulat!")
                    print("   \t\t\t\t\t\t  Fibonacci at indeks '{}' could not be found".format(e))
                    print("[!]Type Error\t\t\t: {}".format(str(type(e))[8:(len(str(type(e))) - 2)]))
                    print("[!]Detail Error\t\t\t: iterasi tidak dapat mencari deret fibbonaci pada indeks yang bernilai float")

        print(100 * "-")


#MAIN PROGRAM
if __name__ == '__main__':
    print(100 * "=")
    print("{:^100}".format("PERHITUNGAN DENGAN ITERASI"))
    print(100 * "=")
    loop = 'y'

    while ((loop == 'y') or (loop == 'Y')):
        print()
        print(100 * "-")
        try :
            pilihan = input("[>]Pilihan Perhitungan\t: "
                                    "[1]PANGKAT\n\t\t\t\t\t\t  "
                                    "[2]FAKTORIAL\n\t\t\t\t\t\t  "
                                    "[3]FIBONACCI\n"
                                    "[>]Masukkan Pilihan\t\t:  ")

            print(100 * "-")
            print(100 * "-")

            program = iterasi(pilihan)
            program.perhitungan()
            loop = ' '
            if iterasi.error == False :
                loop = input("[?]Ingin mengulang kembali perhitungan?(y/t): ")
            del program
            print()

        except EOFError as e:
            print()
            print("[!]Error Massage\t\t: Terjadi kesalahan input, program keluar secara paksa!")
            print("[!]Type Error \t\t\t: {}".format(str(type(e))[8:(len(str(type(e))) - 2)]))
            print("[!]Detail Error \t\t: {}".format(e))
            print(100 * "-")
            break

    print(100 * "=")