#Operasi iterasi
#Modul ini dapat digunakan dengan melakukan import package yang menyimpan modul ini

print("Note : Modul opeasiIterasi dapat digunakan!\n")

def operasiPangkat(angka, pangkat) :
    hasil = angka
    print("Operasi Hitung\t\t:", angka, end='')
    for i in range(1, (pangkat)):
        print(" * ", angka, end='')
        hasil *= angka
    print("\nHasil Hitung\t\t:", hasil)

def operasiFaktorial(angka) :
    hasil = angka
    print("Operasi Hitung\t\t:", angka, end='')
    for i in reversed(range(1, (angka))):
        print(" * ", i, end='')
        hasil *= i
    print("\nHasil Hitung\t\t:", hasil)

def operasiFibonacci(deret) :
    buffer1 = int(0)
    buffer2 = int(1)
    buffer3 = buffer1 + buffer2
    print("Deret Fibonacci\t\t:", buffer1, " | ", buffer2, end='')
    for i in range(2, (deret + 1)):
        buffer3 = buffer1 + buffer2;
        print(" | ", buffer3, end='')
        buffer1 = buffer2
        buffer2 = buffer3
    hasil = buffer3
    print("\nFibonacci ke-{}\t\t: {}".format(deret, hasil))