#DEKLARASI CLASS
class iterasi :

    print(60 * "=")
    print("{:^60}".format("PERHITUNGAN DENGAN ITERASI"))
    print((60 * "=") + "\n")

    def __init__(self):
        print(60 * "=")
        print(60 * "-")
        iterasi.pilihan = int(input("Pilihan\t: [1]PANGKAT\n\t\t  [2]FAKTORIAL\n\t\t  [3]FIBONACCI\nPilih\t:  "))
        print(60 * "-")
        print(60 * "-")
        if iterasi.pilihan is 1 :
            self.angka = eval(input("Masukkan Angka\t\t: "))
            self.pangkat = eval(input("Masukkan Pangkat\t: "))

        elif iterasi.pilihan is 2 :
            self.angka = eval(input("Masukkan Angka\t\t: "))

        elif iterasi.pilihan is 3 :
            self.deret = eval(input("Masukkan Deret\t\t: "))

        else :
            print("Pilihan yang dimasukkan salah!")

    def perhitungan(self):

        if iterasi.pilihan is 1:
            self.hasil = self.angka
            print("Operasi Hitung\t\t:", self.angka, end='' )
            for i in range(1,(self.pangkat)) :
                print(" * ", self.angka, end='')
                self.hasil *= self.angka
            print("\nHasil Hitung\t\t:", self.hasil)

        elif iterasi.pilihan is 2:
            self.hasil = self.angka
            print("Operasi Hitung\t\t:", self.angka, end='')
            for i in reversed(range(1, (self.angka))):
                print(" * ", i, end='')
                self.hasil *= i
            print("\nHasil Hitung\t\t:", self.hasil)

        elif iterasi.pilihan is 3 :
            buffer1 = int(0)
            buffer2 = int(1)
            buffer3 = buffer1 + buffer2
            print("Deret Fibonacci\t\t:", buffer1, " | ", buffer2, end='')
            for i in range(2, (self.deret+1)):
                buffer3 = buffer1 + buffer2;
                print(" | ", buffer3, end='')
                buffer1 = buffer2
                buffer2 = buffer3
            self.hasil = buffer3
            print("\nFibonacci ke-{}\t\t: {}".format(self.deret,self.hasil))

        print(60 * "-")
        print(60 * "=")

#MAIN PROGRAM
loop = 'y'
while (loop == 'y') or (loop == 'Y') :
    program = iterasi()
    program.perhitungan()
    loop = input("Ingin mengulang kembali perhitungan?(y/t): ")
    del program
    print("\n")