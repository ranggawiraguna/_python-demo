#lambdaFunction >> defFunction sederhana with return value

#lambdaFunction
function1 = lambda : "[>]RANGGA WIRAGUNA"

#lambdaFunction
function2 = lambda : print("[>]RANGGA WIRAGUNA")

#lambdaFunction
function3 = lambda : (print("[>]RANGGA WIRAGUNA",end=''),print("(1803015106)"))

#lambdaFunction with argumen
function4 = lambda teks :  print(teks)

#lambdaFunction with argumen keyword
function5 = lambda nama,nim,jurusan : (print("[>]Nama\t\t:", nama),print("   NIM\t\t:", nim),print("   Jurusan\t:", jurusan))

#lambdaFunction with default argumen keyword
function6 = lambda nama,nim,jurusan='TEKNIK' : "[>]Nama\t\t:{}\n   NIM\t\t:{}\n   Jurusan\t:".format(nama,nim,jurusan)

#lambdaFinction with argumen sembarang
function7 = lambda *tempTuple : sum(tempTuple)

#lambdaFunction with fix argumen & argumen sembarang
function8 = lambda angka,*tempTuple : str(angka) + " | " + str(sum(tempTuple))

#lambdaFunction with fix default argumen & argumen sembarang
function9 = lambda angka=100,*tempTuple : str(angka) + " | " + str(sum(tempTuple))

def panggilSemua() :
    #Pemanggilan function1()
    print("lambdaFunction1()")
    returnValue = function1()
    print(returnValue)
    print(function1())
    print()

    #Pemanggilan function2()
    print("lambdaFunction2()")
    function2()
    print()

    #Pemanggilan function3()
    print("lambdaFunction3()")
    function3()
    print()

    #Pemanggilan function4()
    print("lambdaFunction4()")
    function4("[>]Teknik Informatika")
    print()

    #Pemanggilan function5()
    print("lambdaFunction5()")
    function5("Rangga Wiraguna", "1803015106", "Teknik Informatika")
    function5(nim="1803015106", jurusan="Teknik Informatika",nama="Rangga Wiraguna")
    print()

    #Pemanggilan function6()
    print("lambdaFunction6()")
    print(function6("Rangga Wiraguna", "1803015106"))
    print(function6("Rangga Wiraguna", "1803015106", "Teknik Informatika"))
    print(function6(nim="1803015106", jurusan="Teknik Informatika",nama="Rangga Wiraguna"))
    print(function6(nim="1803015106", nama="Rangga Wiraguna"))
    print()

    #Pemanggilan function7()
    print("lambdaFunction7()")
    print("[>]Jumlah :",function7(10))
    print("   Jumlah :",function7(10,20))
    print("   Jumlah :",function7(10,20,30))
    print("   Jumlah :",function7(10,20,30,40))
    print("   Jumlah :",function7(10,20,30,40,50))
    print()

    #Pemanggilan function8()
    print("lambdaFunction8()")
    print("[>]Jumlah :",function8(10))
    print("   Jumlah :",function8(10,20))
    print("   Jumlah :",function8(10,20,30))
    print("   Jumlah :",function8(10,20,30,40))
    print("   Jumlah :",function8(10,20,30,40,50))
    print()

    #Pemanggilan function9()
    print("lambdaFunction9()")
    print("[>]Jumlah :",function9(10))
    print("   Jumlah :",function9(10,20))
    print("   Jumlah :",function9(10,20,30))
    print("   Jumlah :",function9(10,20,30,40))
    print("   Jumlah :",function9(10,20,30,40,50))

if __name__ == "__main__" :
    panggilSemua()

    print("\n")
    #Method untuk lambdaFunction
    print("Method untuk lambdaFunction")
    list1 = [2,5,7,9,13,18,22,26,28,29]
    list2 = [1,4,5,8,11,15,18,23,26,30]
    lambda1 = lambda x : (x%2)==0
    lambda2 = lambda x : x*10

    #filter() membutuhkan lambda return boolean untuk menyaring anggota list yang bernilai true jika dijadikan argumen pada lambda
    #jika lambda menghasilkan true maka value dari list iterable nya akan dimasukkan dalam list baru untuk dijadikan hasil filter
    #return new list
    listBuffer = list(filter(lambda1, list1))
    print("[>]Hasil Filter :", listBuffer)
    listBuffer = list(filter(lambda x : x%2 == 0, list1))
    print("   Hasil Filter :", listBuffer)
    print("   Hasil Filter :", list(filter(lambda1, list2)))
    print("   Hasil Filter :", list(filter(lambda x : x%2 == 0, list2)))

    print()

    #map() akan menghasilkan value yang di return lambda berdasarkan argumen list sebagai iterablenya dan disimpan dalam sebuah list baru
    #return new list
    listBuffer = list(map(lambda2, list1))
    print("[>]Hasil Operasi :", listBuffer)
    listBuffer = list(map(lambda x : x*10, list1))
    print("   Hasil Operasi :", listBuffer)
    print("   Hasil Operasi :", list(map(lambda2, list2)))
    print("   Hasil Operasi :", list(map(lambda x : x*10, list2)))

