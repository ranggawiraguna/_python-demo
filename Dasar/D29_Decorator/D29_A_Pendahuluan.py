def cekErrorPembagian(func):

    def pembagianNew(x,y,z=1) :
        if (type(x) is not int) or (type(y) is not int) or (type(z) is not int) :
            print("Nilai pembilang/penyebut harus berupa angka!")
            return

        elif (y==0) or (z==0):
            print("Nilai pembagi tidak boleh sama dengan nol")
            return

        else :
            if "pembagian2" in str(func) :
                print("({}/{}) =".format(x,y), end=' ')
                return func(x,y)
            elif "pembagian3" in str(func) :
                print("({}/{})/{} =".format(x,y,z), end=' ')
                return func(x,y,z)

    return pembagianNew

# Pada statement ini fungsi akan didekorasi ulang pada fungsiDecorator, artinya fungsi yang menggunakan property akan digantikan oleh
# suatu fungsi yang di return pada fungsiDecorator, dan variableLokal pada fungsi aslinya akan disimpan argumen fungsi yang baru
@cekErrorPembagian  #property ini mengambil fungsi dibawahnya untuk di dekorasi >> pembagian(a,b) = pembagianNew(x=a, y=b, z=1?)
def pembagian2(a,b) :
    hasil = a/b
    return hasil

@cekErrorPembagian  #property ini mengambil fungsi dibawahnya untuk di dekorasi >> pembagian(a,b,c) = pembagianNew(x=a, y=b, z=c)
def pembagian3(a,b,c) :
    hasil = (a/b)/c
    return hasil


if __name__ == '__main__':

    print(50*'=')
    print(50*'-')
    print(pembagian2(10,2))
    print(50*'-')

    print(50*'-')
    print(pembagian2(10,2,5))
    print(50*'-')

    print(50*'=')
    print(pembagian2(10,0))
    print(50*'-')

    print(50*'-')
    print(pembagian2(10,'r'))
    print(50*'-')
    print(50*'=')

    print("\n\n")

    print(50*'=')
    print(50*'-')
    print(pembagian3(10,2,3))
    print(50*'-')

    print(50*'=')
    print(pembagian3(10,0,2))
    print(50*'-')

    print(50*'=')
    print(pembagian3(10,2,0))
    print(50*'-')

    print(50*'-')
    print(pembagian3(10,'r',1))
    print(50*'-')
    print(50*'=')