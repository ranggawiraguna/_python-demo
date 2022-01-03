# Rekursi
# Sebuah fungsi yang dapat memanggil dirinya sendiri sampai pada batasan tertentu yang di tetapkan didalam fungsi tersebut

def faktorial(angka) :

    if((angka is 0) or (angka is 1)) :
        return angka

    else :
        return angka * faktorial(angka-1)

def bilPangkat(angka, pangkat) :

    if(pangkat is 0) :
        return 1

    else :
        return angka * bilPangkat(angka, pangkat-1)

def fibonacci(deret) :

    if((deret is 0) or (deret is 1)) :
        return deret

    else :
        return fibonacci(deret-1) + fibonacci(deret-2)


if __name__ == '__main__':
    print(100*'=')
    x = int(input("[>]Masukkan Angka   : "))
    print("[>]Hasil Faktorial  :", faktorial(x))
    print(100*'=')

    print(100*'=')
    x = int(input("[>]Masukkan Angka   : "))
    y = int(input("[>]Masukkan Pangkat : "))
    print("[>]Hasil bilPangkat :", bilPangkat(x, y))
    print(100*'=')

    print(100*'=')
    x = int(input("[>]Masukkan Deret   : "))
    print("[>]Hasil Fibbonacci :", fibonacci(x))
    print(100*'=')

