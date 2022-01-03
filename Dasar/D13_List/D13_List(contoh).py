#LIST
#Kumpulan data, bersifat MUTABLE artinya anggota dari list dapat dirubah ataupun dihapus

#Deklarasi list
list1 = [60, 78, 77, 88, 84, 90, 72, 80]
list2 = [16, 28, 11, 29, 19, 37, 21, 23]
buffer = []

data1 = [57,70,96,78,65,66,79,80,70,88]
data2 = [80,77,56,40,81,79,66,80,80,90]
data3 = [data1, None, data2]
data4 = [data1+data2]
data5 = list("INFORMATIKA")
buffer2 = []

#MENYATUKAN LIST
print(120*"=")
print("MENYATUKAN LIST\n")

buffer = list1      #Menyatukan kedua list dalam alamat memori yang sama
print("[>]list1  = " + str(list1))
print("[>]buffer = " + str(buffer))
print()

list1[1] = 97       #Mengubah list1[1] menjadi 97, yang berpengaruh juga pada buffer[1]
buffer[2] = 56      #Mengubah buffer[2] menjadi 56, yang berpengaruh juga pada list1[2]

print("[>]list1  = " + str(list1))
print("[>]buffer = " + str(buffer))
print()

#MENGCOPY SEMUA ELEMEN LIST
print(120*"=")
print("MENGCOPY SEMUA LIST\n")

buffer = list1[:]      #Mengcopy list dari indek awal-akhir, tidak menyatukan pada alamat memori yang sama
print("[>]list1  = " + str(list1))
print("[>]buffer = " + str(buffer))
print()

list1[2] = 77       #Mengubah list1[2] menjadi 77
buffer[2] = 99      #Mengubah buffer[2] menjadi 99

print("[>]list1  = " + str(list1))
print("[>]buffer = " + str(buffer))
print()

#MENGCOPY SEBAGIAN ELEMEN LIST
print(120*"=")
print("MENGCOPY SEBAGIAN LIST\n")

buffer = list1[1:6]      #Mengcopy list dari indek awal s/d --akhir
print("[>]list1  = " + str(list1))
print("[>]buffer = " + str(buffer))
print()

#MENAMBAHKAN BEBERAPA LIST MENJADI SATU LIST
print(120*"=")
print("MENAMBAHKAN LIST\n")

buffer = list1 + list2      #Menambahkan kedua list di dalam satu list
print("[>]list1  = " + str(list1))
print("[>]list2  = " + str(list2))
print("[>]buffer = " + str(buffer))
print()

#Merubah isi list dengan slicing
print(120*"=")
print("MERUBAH ISI LIST DENGAN SLICING\n")

print("[>]list1  = " + str(list1))
list1[2:6] = [45, 54, 67, 72]      #Merubah elemen list dari indeks awal s/d --akhir
print("[>]list1  = " + str(list1))
print(120*"=")
print()

#Mengisi list secara berulang
print(120*"=")
print("MENGISI LIST SECARA BERULANG\n")

buffer = list1[0:2] * 4     #Mengisi list dengan mengambil list lain dari indeks awal s/d --akhir sebanyak 4-kali
print("[>]list1  = " + str(list1))
print("[>]buffer = " + str(buffer))
print(120*"=")
print()

#MENGABUNGKAN BEBERAPA LIST MENJADI SATU LIST MULTIDIMENSI
print(120*"=")
print("MENGGABUNGKAN LIST\n")

buffer = [list1, list2]      #Mnggabungkan kedua list di dalam satu list multidimensi
print("[>]list1  = " + str(list1))
print("[>]list2  = " + str(list2))
print("[>]buffer = " + str(buffer))
print(120*"=")
print()

#Function & Method untuk list
print(120*"=")
print("FUNCTION & METHOD UNTUK LIST\n")

print("[>]Banyak elemen pada list1 adalah " + str(len(list1)) + "\n")

print("[>]list1 nilai awal      = " + str(list1))
list1.append(100)                               #Menambahkan anggota(100) kedalam list1 akhir
print("[>]list1 append(100)     = " + str(list1))
list1.insert(5, 50)                             #Menambahkan anggota9(50) di indeks ke-5 pada list
print("[>]list1 insert(5, 50)   = " + str(list1))
del list1[4]                                    #Menghapus isi dari list di elemen ke-4
print("[>]function del list1[4] = " + str(list1))

#Function & Method lain untuk list
print(120*"=")
print("FUNCTION & METHOD LAIN UNTUK LIST")

#Apakah isi list ada isinya di setiap elemen(tidak ada yang kosong) >> return boolean
print("[>]Apakah list data2 memiliki nilai disetiap anggotanya?\n   ({})".format(all(data2)))
print("[>]Apakah list data3 memiliki nilai disetiap anggotanya?\n   ({})".format(all(data3)))
print("[>]Apakah list data5 memiliki nilai disetiap anggotanya?\n   ({})\n".format(all(data5)))

#Melihat isi list ada isinya atau tidak(minimal ada satu isi) >> return boolean
print("[>]Apakah list data3 memiliki minimal satu nilai dari semua anggotanya?\n   ({})".format(any(data3)))
print("[>]Apakah list buffer2 memiliki minimal satu nilai dari semua anggotanya?\n   ({})".format(any(buffer2)))
print("[>]Apakah list data5 memiliki minimal satu nilai dari semua anggotanya?\n   ({})\n".format(any(data5)))

#Melihat panjang dari list >> return int
print("[>]Berapa panjang dari list data1?\n   ({}-elemen)".format(len(data1)))
print("[>]Berapa panjang dari list data3?\n   ({}-elemen)".format(len(data3)))
print("[>]Berapa panjang dari list data5?\n   ({}-elemen)\n".format(len(data5)))

#Melihat nilai maximum dari list >> return sesuai tipedata anggota max
print("[>]Berapa nilai maximum dari list data2?\n   (Max = {})".format(max(data2)))
print("[>]Berapa nilai maximum dari list data4?\n   (Max = {})".format(max(data4)))
print("[>]Berapa nilai maximum dari list data5?\n   (Max = {})\n".format(max(data5)))

#Melihat nilai minimum dari list >> return sesuai tipedata anggota min
print("[>]Berapa nilai minimum dari list data1?\n   (Min = {})".format(min(data1)))
print("[>]Berapa nilai minimum dari list data4?\n   (Min = {})".format(min(data4)))
print("[>]Berapa nilai minimum dari list data5?\n   (Min = {})\n".format(min(data5)))

#Mengurutkan data list >> return list terurut
print("[>]Nilai Awal data1\t: {}\n   Data1 Sorted()\t: {}".format(data1,sorted(data1)))
print("[>]Nilai Awal data4\t: {}\n   Data4 Sorted()\t: {}".format(data4,sorted(data4)))
print("[>]Nilai Awal data5\t: {}\n   Data5 Sorted()\t: {}\n".format(data5,sorted(data5)))

#Menjumlahkan semua data list >> return int
print("[>]Data1 : {}\n   Total : {}".format(data1,sum(data1)))
print("[>]Data2 : {}\n   Total : {}\n".format(data2,sum(data2)))

print(120*"=")