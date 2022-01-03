#Function
def function1() :
    """def function1()"""
    print("[>]RANGGA WIRAGUNA")

#Function with argumen
def function2(teks) :
    """def function2()"""
    print(teks)

#Function with argumen keyword
def function3(nama,nim,jurusan) :
    """def function3()"""
    print("[>]Nama\t\t:", nama)
    print("   NIM\t\t:", nim)
    print("   Jurusan\t:", jurusan)

#Function with default argumen
def function4(teks="Kosong") :
    """def function4()"""
    print("[>]"+teks)

#Function with argumen & return value
def function5(angka1,angka2) :
    """def function5()"""
    hasil = angka1 + angka2
    return hasil

#Function with default argumen & return value
def function6(angka,pangkat=1) :
    """def function6()"""
    hasil = angka ** pangkat
    return hasil

#Function with argumen sembarang
def function7(*tempTuple) :
    """def function7()"""
    jumlah = int()
    for i in range(len(tempTuple)) :
        jumlah += tempTuple[i]
    print("[>]Jumlah Keseluruhan :", jumlah)

#Function with argumen fix & argumen sembarang
def function8(angka1,*tempTuple) :
    """def function8()"""
    print("[>]Angka1 :", angka1)
    for i in range(len(tempTuple)) :
        print("   Angka{} : {}".format((i+2),tempTuple[i]))

#Function with default argumen fix & sembarang
def function9(angka1=1,*tempTuple) :
    """def function9()"""
    print("[>]Angka1 :", angka1)
    for i in range(len(tempTuple)) :
        print("   Angka{} : {}".format((i+2),tempTuple[i]))

#Function in Function
def panggilSemuaFungsi() :
    # Pemanggilan function1()
    print(function1.__doc__)
    function1()
    print()

    # Pemanggilan function2()
    print(function2.__doc__)
    function2("1803015106")
    print()

    # Pemanggilan function3()
    print(function3.__doc__)
    function3("Rangga Wiraguna" , "1803015106" , "Teknik Informatika")
    function3(jurusan="Teknik Informatika", nim="1803015106", nama="Rangga Wiraguna")
    print()

    # Pemanggilan function4()
    print(function4.__doc__)
    function4()
    function4("Teknik Informatika")
    print()

    # Pemanggilan function5()
    print(function5.__doc__)
    angka = function5(10,20)
    print("[>]Hasil Penambahan 10 + 20 = ", angka)
    print("[>]Hasil Penambahan 10 + 20 = ", function5(10,20))
    print()

    # Pemanggilan function6()
    print(function6.__doc__)
    angka = function6(4)
    print("[>]Hasil Pangkat = ", angka)
    print("[>]Hasil Pangkat = ", function6(4, 2))
    print()

    # Pemanggilan function7()
    print(function7.__doc__)
    function7(10)
    function7(10, 20)
    function7(10, 20, 30)
    print()

    # Pemanggilan function8()
    print(function8.__doc__)
    function8(10)
    function8(10, 20)
    function8(10, 20, 30)
    print()

    # Pemanggilan function9()
    print(function9.__doc__)
    function9()
    function9(10)
    function9(10, 20)
    function9(10, 20, 30)
    print()

#Main Program
if __name__ == "__main__" :
    panggilSemuaFungsi()


