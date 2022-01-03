# Closure
# Sebuah fungsi bersarang yang dapat digunakan seperti sebuah class sederhana
# pada closure objek yang mendapatkan return sebuah fungsi, objek akan menjadi sebuah fungsi yang sama dengan fungsi yang di return,
# dan objek yang dibentuk telah menyimpan variable non-lokal yang ada pada fungsi induknya pada saat terakhir dijanlankan

def bilangan(x) :
    angka = x

    print("BILANGAN PANGKAT", angka)

    def hitungPangkat(y) :  # karena fungsi ini menggunakan variable non-lokal yaitu angka, jadi pada saat di kembalikan pada sebuah objek, objek tersebut sekaligus menyimpan variable berserta value yang pada fungsi induknya
        pangkat = y
        if pangkat >= 0 :
            value = angka ** pangkat
            print("[>] bilanganPangkat({}) adalah".format(pangkat), end=' ')
            return value
        else :
            raise IndexError

    return hitungPangkat #mengembalikan sebuah fungsi yang dapat disimpan pada sebuah objek baru


if __name__ == '__main__':
    print(100*'=')
    bilanganPangkat = bilangan(5)    #Menyimpan nilai return pada fungsi kelipatan dengan argumen 10

    print("[>] bilanganPangkat adalah", type(bilangan), "bilangan(5).hitungPangkat(y)")

    try :
        print(bilanganPangkat(4)) # Menggunakan objek bilangan sebagai fungsi index dengan argumen 20
    except IndexError :
        print("[>] bilanganPangkat(4) adalah tidak tersedia")

    print(100*'=')


    print(100 * '=')
    bilanganPangkat = bilangan(5)    #Menyimpan nilai return pada fungsi kelipatan dengan argumen 10

    print("[>] bilanganPangkat adalah", type(bilangan), "bilangan(5).hitungPangkat(y)")

    try:
        print(bilanganPangkat(-1))  # Menggunakan objek bilangan sebagai fungsi index dengan argumen 20
    except IndexError:
        print("[>] bilanganPangkat(-1) adalah tidak tersedia")

    print(100 * '=')


