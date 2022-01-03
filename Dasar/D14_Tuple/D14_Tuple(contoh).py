#TUPLE
#bersifat IMMUTABLE artinya anggota tidak dapat dirubah ataupun dihapis, kecuali untuk keseluruhannya(1-tuple)
#kecuali jika dalam suatu tuple terdapat list, maka anggota list tersebut dapat dirubah ataupun dihapus

#Deklarasi tuple
data1 = (57,70,96,78,65,66,79,80,70,88)
data2 = (80,77,56,40,81,79,66,80,80,90)
data3 = (list(data1), None, list(data2))
data4 = (list(data1)+list(data2))
data5 = tuple("INFORMATIKA")
buffer = ()

#Mengakses tuple
#Tuple akan memberikan nilai secara berurut
a,b,c,d,e,f,g,h,i,j = data1
print(120*"=")
print("MENGAMBIL NILAI TUPLE\n")
print("[>]abcdefghij    = ({},{},{},{},{},{},{},{},{},{})".format(a,b,c,d,e,f,g,h,i,j))
del a,b,c,d,e,f,g,h,i,j
print("[>]data1[0]      =", data1[0])
print("[>]data1[8]      =", data1[8])
print("[>]data1[2:8]    =", data1[2:8])
print("[>]data2[0][2:8] =", data3[0][2:8])
print("[>]data2[2][2:8] =", data3[2][2:8])

#Memeriksa suatu nilai pada tuple
print(120*"=")
print("MEMERIKSA SUATU NILAI PADA TUPLE\n")
print("[>]Apakah 70 ada dalam data1? ({})".format(70 in data1))
print("[>]Apakah 77 ada dalam data1? ({})".format(77 in data1))
print("[>]Apakah 70 tidak ada dalam data1? ({})".format(70 not in data1))
print("[>]Apakah 77 tidak ada dalam data1? ({})".format(77 not in data1))

#Tuple sebagai iterable
print(120*"=")
print("For in tuple\n")
index = 0;
for i in data1 :
    print("Nilai-{} : {}".format(index, i))
    index += 1

#Method&Fungsi Bawaan Tuple
print(120*"=")
print("Method dan Fungsi bawaan\n")
print("[>]Banyak angka 70 pada data1 adalah {}".format(data1.count(70))) #Memeriksa banyak anggota yang bernilai tertentu
print("   Indeks angka 70 pada data1 adalah {}".format(data1.index(70))) #Memeriksa indeks dari anggota yang bernilai tertentu
print("[>]Banyak angka 80 pada data1 adalah {}".format(data2.count(80))) #Memeriksa banyak anggota yang bernilai tertentu
print("   Indeks angka 80 pada data1 adalah {}".format(data2.index(80))) #Memeriksa indeks dari anggota yang bernilai tertentu

print(120*"=")
#Apakah isi tuple ada isinya di setiap elemen(tidak ada yang kosong) >> return boolean
print("METHOD LAIN UNTUK TUPLE\n")
print("[>]Apakah tuple data2 memiliki nilai disetiap anggotanya?\n   ({})".format(all(data2)))
print("[>]Apakah tuple data3 memiliki nilai disetiap anggotanya?\n   ({})".format(all(data3)))
print("[>]Apakah tuple data5 memiliki nilai disetiap anggotanya?\n   ({})\n".format(all(data5)))

#Melihat isi tuple ada isinya atau tidak(minimal ada satu isi) >> return boolean
print("[>]Apakah tuple data3 memiliki minimal satu nilai dari semua anggotanya?\n   ({})".format(any(data3)))
print("[>]Apakah tuple buffer memiliki minimal satu nilai dari semua anggotanya?\n   ({})".format(any(buffer)))
print("[>]Apakah tuple data5 memiliki minimal satu nilai dari semua anggotanya?\n   ({})\n".format(any(data5)))

#Melihat panjang dari tuple >> return int
print("[>]Berapa panjang dari tuple data1?\n   ({}-elemen)".format(len(data1)))
print("[>]Berapa panjang dari tuple data3?\n   ({}-elemen)".format(len(data3)))
print("[>]Berapa panjang dari tuple data5?\n   ({}-elemen)\n".format(len(data5)))

#Melihat nilai maximum dari tuple >> return sesuai tipedata anggota max
print("[>]Berapa nilai maximum dari tuple data2?\n   (Max = {})".format(max(data2)))
print("[>]Berapa nilai maximum dari tuple data4?\n   (Max = {})".format(max(data4)))
print("[>]Berapa nilai maximum dari tuple data5?\n   (Max = {})\n".format(max(data5)))

#Melihat nilai minimum dari tuple >> return sesuai tipedata anggota min
print("[>]Berapa nilai minimum dari tuple data1?\n   (Min = {})".format(min(data1)))
print("[>]Berapa nilai minimum dari tuple data4?\n   (Min = {})".format(min(data4)))
print("[>]Berapa nilai minimum dari tuple data5?\n   (Min = {})\n".format(min(data5)))

#Mengurutkan data tuple >> return list terurut
print("[>]Nilai Awal data1\t: {}\n   Data1 Sorted()\t: {}".format(data1,tuple(sorted(data1))))
print("[>]Nilai Awal data4\t: {}\n   Data4 Sorted()\t: {}".format(data4,tuple(sorted(data4))))
print("[>]Nilai Awal data5\t: {}\n   Data5 Sorted()\t: {}\n".format(data5,tuple(sorted(data5))))

#Menjumlahkan semua data tuple >> return int
print("[>]Data1 : {}\n   Total : {}".format(data1,sum(data1)))
print("[>]Data2 : {}\n   Total : {}\n".format(data2,sum(data2)))

print(120*"=")