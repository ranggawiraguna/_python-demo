class fibonacci :

    def __init__(self, angka):
        self.deret = [0,1]
        self.cari = angka

    def hitung(self):
        try:
            if ((self.cari % 1) != 0) :
                self.hasilCari = None
                raise ValueError(self.cari)

            i = self.cari
            for i in range(2, (self.cari + 1)):
                self.deret.append(self.deret[i-1] + self.deret[i-2])

            self.hasilCari = self.deret[i]

        except (AttributeError,SyntaxError,NameError,EOFError,KeyboardInterrupt) as e:
            print()
            print("[!]Error Message\t\t: Masukkan input dengan benar!")
            print("[!]Type Error\t\t\t: {}".format(str(type(e))[8:(len(str(type(e)))-2)]))
            print("[!]Detail Error\t\t\t: {}".format(e))

        except ValueError as e:
            print()
            print("[!]Error Message\t\t: Masukkan Deret dengan bilangan bulat!")
            print("   \t\t\t\t\t\t  Fibonacci at indeks '{}' could not be found".format(e))
            print("[!]Type Error\t\t\t: {}".format(str(type(e))[8:(len(str(type(e))) - 2)]))

    def tampilkanDeret(self):
        try:
            if (len(self.deret)+1 > 16) :
                print(75 * "-")
                print("Deret Fibonacci: ")
                for i in range(16):
                    print(" ", self.deret[i], end='')
                print()
                print(75 * "-")
                print("Deret Fibanacci ke-{}  : {} ".format(self.cari, self.hasilCari))
                print(75 * "-")

            else :
                if self.hasilCari != None:
                    print(75 * "-")
                    print("Deret Fibonacci: ")
                    for i in range(len(self.deret)):
                        print(" ", self.deret[i],end='')

                    print()
                    print(75 * "-")
                    print("Deret Fibanacci ke-{}  : {} ".format(self.cari,self.hasilCari))
                    print(75 * "-")

            assert (self.cari <= 15), self.cari

        except AssertionError as e:
            print("[!]Error Message\t\t: Deret hanya bisa ditampilkan sampai indeks-15!")
            print("   \t\t\t\t\t\t  Fibonacci at indeks '{}' exceed the limit".format(e))
            print("[!]Type Error\t\t\t: {}".format(str(type(e))[8:(len(str(type(e))) - 2)]))
