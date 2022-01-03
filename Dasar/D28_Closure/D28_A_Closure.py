# Closure
# Sebuah fungsi bersarang yang dapat digunakan seperti sebuah class sederhana
# pada closure objek yang mendapatkan return sebuah fungsi, objek akan menjadi sebuah fungsi yang sama dengan fungsi yang di return,
# dan objek yang dibentuk telah menyimpan variable non-lokal yang ada pada fungsi induknya pada saat terakhir dijanlankan

def kelipatan(x) :
    angka = x

    print("BILANGAN KELIPATAN", angka)

    def deret(y) :  # karena fungsi ini menggunakan variable non-lokal yaitu angka, jadi pada saat di kembalikan pada sebuah objek, objek tersebut sekaligus menyimpan variable berserta value yang pada fungsi induknya
        index = y
        if index > 0 :
            value = angka * index
            print("[>] bilangan({}) adalah".format(index), end=' ')
            return value
        else :
            raise IndexError

    return deret #mengembalikan sebuah fungsi yang dapat disimpan pada sebuah objek baru


if __name__ == '__main__':
    print(100*'=')
    bilanganKelipatan = kelipatan(5)    #Menyimpan nilai return pada fungsi kelipatan dengan argumen 10

    print("[>] bilanganKelipatan adalah", type(bilanganKelipatan), "kelipatan(5).deret(y)")

    try :
        print(bilanganKelipatan(10)) # Menggunakan objek bilangan sebagai fungsi index dengan argumen 20
    except IndexError :
        print("[>] bilanganKelipatan(10) adalah tidak tersedia")

    print(100*'=')


    print(100 * '=')
    bilanganKelipatan = kelipatan(10)  # Menyimpan nilai return pada fungsi kelipatan dengan argumen 10

    print("[>] bilangan adalah", type(bilanganKelipatan), "kelipatan(10).deret(y)")

    try:
        print(bilanganKelipatan(-1))  # Menggunakan objek bilangan sebagai fungsi index dengan argumen 20
    except IndexError:
        print("[>] bilangan(-1) adalah tidak tersedia")

    print(100 * '=')
