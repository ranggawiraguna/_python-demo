# Generator
# Fungsi yang mengimplementasikan iterator dengan cara yang sederhana
# Berisi setidaknya satu keywoard yield untuk mempause statement pada saat pemanggilan fungsi, dan dapat dilanjutkan pada saat yield terakhir,
# Ketika melanjutkan pemanggilan fungsi pada yield terakhir value terakhir pada variable lokal didalam fungsi masih tetap tersimpan.
# Jika pada fungsi biasa value pada variable lokal dihancurkan pada saat fungsi telah selesai dijalankan, maka pada fungsi generator,
# yield akan mempause sementara sebuah fungsi, dan statement akan dilanjutkan pada yield terakhir jika fungsi dipanggil kembali dan
# value pada variable lokal masih tetap tersimpan

def generator1() :
   #next[0]
    iter = 0
    value = 2 ** iter
    print(iter, ">>", end=' ')
    yield value

   #next[1]
    iter += 1
    value = 2 ** iter
    print(iter, ">>", end=' ')
    yield value

   #next[2]
    iter += 1
    value = 2 ** iter
    print(iter, ">>", end=' ')
    yield value

   #next[3]
    iter += 1
    print(iter, ">>", end=' ')
    value = 2 ** iter
    yield value


def generator2(maxIter) :
    iter = 0
    value = 1

    for i in range (maxIter) :
       #next[iter]
        print(iter, ">>", end=' ')
        yield value

        iter += 1
        value = 2 ** iter


if __name__ == '__main__':

    object_generator1 = generator1()

    print(50*'=')
    for yieldGen in object_generator1 :
        print(yieldGen)
    print(50*'=')
   #next(object_generator1) >> error StopIteration



    object_generator2 = generator2(10)

    print(50*'=')
    for yieldGen in object_generator2 :
        print(yieldGen)
    print(50*'=')
    #next(object_generator2) >> error StopIteration

