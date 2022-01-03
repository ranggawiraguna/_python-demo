#SET
#Bersifat mutable, tapi karena set tidak menggunakan indeks di setiap elemennya
#maka mustahil mengubah anggota elemen didalamnya
#Set tidak boleh berisi list didalamnya

#Deklarasi set
data1 = {57,70,96,78,65,66,79,80,70,88}
data2 = {80,77,56,40,81,79,66,80,80,90}
data3 = {tuple(data1), None, tuple(data2)}
data4 = {tuple(data1)+tuple(data2)}
data5 = set("INFORMATIKA") #Teks "INFORMATIKA" akan dimasukkan per karakter kedalam set secara acak
buffer = set()

#Menambahkan anggota pada set >> return None >> Menambahkan langsung elemen set
#add(all)
#update(str/list/tuple)
print(80*"=")
print("MENAMBAHKAN ANGGOTA PADA SET\n")

print("[>]Data1 awal      : {}".format(data1))
data1.add(100)                              #Menambahkan argumen kedalam set secara acak
print("   Data1.add()     : {}".format(data1))
print("[>]Data2 awal      : {}".format(data2))
data2.add(100)                              #Menambahkan argumen kedalam set secara acak
print("   Data2.add()     : {}\n".format(data2))

print("[>]Data1 awal      : {}".format(data1))
data1.update([0,90])                           #Menambahkan argumen kedalam set secara acak, list akan diurakaian per elemen
print("   Data1.update()  : {}".format(data1))
print("[>]Data2 awal      : {}".format(data2))
data2.update((0,89))                           #Menambahkan argumen kedalam set secara acak, tuple akan diuraikanper elemen
print("   Data2.update()  : {}".format(data2))
print("[>]Data5 awal      : {}".format(data5))
data5.update(("TEKNIK"))                           #Menambahkan argumen kedalam set secara acak, tuple akan langsung dimasukkan dalam bentuk tuple
print("   Data5.update()  : {}".format(data5))

#Menghapus anggota pada set >> return None >> Menghapus langsung elemen set
print(80*"=")
print("MENGHAPUS ANGGOTA PADA SET\n")

print("[>]Data1 awal      : {}".format(data1))
data1.remove(100)                              #Menghapus argumen dari set, error jika argumen tidak ditemukan didalam set
print("   Data1.remove()  : {}".format(data1))
print("[>]Data2 awal      : {}".format(data2))
data2.remove(100)                              #Menghapus argumen dari set, error jika argumen tidak ditemukan didalam set
print("   Data2.remove()  : {}\n".format(data2))

print("[>]Data1 awal      : {}".format(data1))
data1.discard(0)                           #Menghapus argumen value dari set
data1.discard(90)                          #Menghapus argumen value dari set
print("   Data1.discard() : {}".format(data1))
print("[>]Data2 awal      : {}".format(data2))
data2.discard(0)                           #Menghapus argumen value dari set
data2.discard(89)                          #Menghapus argumen value dari set
print("   Data2.discard() : {}".format(data2))
print("[>]Data5 awal      : {}".format(data5))
data5.discard("T"); data5.discard("E"); data5.discard("K"); data5.discard("N"); data5.discard("I"); data5.discard("k");
print("   Data5.discard()  : {}\n".format(data5))

print("[>]Data5 awal      : {}".format(data5))
data5.discard('Z')                          #Menghapus argumen value dari set, tidak error jika argumen tidak ditemukan dalam set
print("   Data5.discard() : {}\n".format(data5))

print("[>]Data5 awal      : {}".format(data5))
data5.pop()                                 #Menghapus acak elemen dari set
print("   Data5.pop()     : {}\n".format(data5))

print("[>]Data5 awal      : {}".format(data5))
data5.clear()                                 #Menghapus keseluruhan elemen set
print("   Data5.clear()   : {}".format(data5))

#Operasi set >> Mengoperasikan set seperti sebuah himpunan
print(80*"=")
print("PENGOPERASIAN SET\n")

A = {12,23,17,33,41}
B = {32,10,12,23,11}

print("[>]Gabungan")    #Menghasilkan set baru hasil dari pengoperasian
print("   ( A | B )  = {}".format((A|B)))
print("   ( B | A )  = {}".format((B|A)))
print("   A.union(B) = {}".format((A.union(B))))
print("   B.union(A) = {}\n".format((A.union(B))))

print("[>]Irisan")    #Menghasilkan set baru hasil dari pengoperasian
print("   ( A & B )         = {}".format((A&B)))
print("   ( B & A )         = {}".format((B&A)))
print("   A.intersection(B) = {}".format((A.intersection(B))))
print("   B.intersection(A) = {}\n".format((A.intersection(B))))

print("[>]Selisih")    #Menghasilkan set baru hasil dari pengoperasian
print("   ( A - B )       = {}".format((A-B)))
print("   ( B - A )       = {}".format((B-A)))
print("   A.difference(B) = {}".format((A.difference(B))))
print("   B.difference(A) = {}\n".format((A.difference(B))))

print("[>]Komplemen")    #Menghasilkan set baru hasil dari pengoperasian
print("   ( A ^ B )                 = {}".format((A^B)))
print("   ( B ^ A )                 = {}".format((B^A)))
print("   A.symmetric_difference(B) = {}".format((A.symmetric_difference(B))))
print("   B.symmetric_difference(A) = {}".format((B.symmetric_difference(A))))

#Method & Fungsi lain untuk set
print(80*"=")
print("Method & fungsi lain untuk set\n")

print("[>]var.copy")    #Mengembalikan set di salin
C = A.copy()
D = B.copy()
print("   A = {}\n   C = {}\n   B = {}\n   D = {}\n".format(A,C,B,D))

print("[>]var1.update(var2)")   #Mengembalikan None, langsung mengubah var1 menjadi hasil gabungan dengan var2
C.update(B)
print("   C.update(D) = {}".format(C))
D.update(A)
print("   D.update(A) = {}\n".format(D))

C = A.copy()
D = B.copy()
print("[>]var1.intersection_update(var2)")   #Mengembalikan None, langsung mengubah var1 menjadi hasil irisan dengan var2
C.intersection_update(B)
print("   C.intersection_update(D) = {}".format(C))
D.intersection_update(A)
print("   D.intersection_update(A) = {}\n".format(D))

C = A.copy()
D = B.copy()
print("[>]var1.diffference_update(var2)")   #Mengembalikan None, langsung mengubah var1 menjadi hasil selisih dengan var2
C.difference_update(B)
print("   C.difference_update(B) = {}".format(C))
D.difference_update(A)
print("   D.difference_update(A) = {}\n".format(D))

C = A.copy()
D = B.copy()
print("[>]var1.symmetric_difference_update(var2)")   #Mengembalikan None, langsung mengubah var1 menjadi hasil komplemen dengan var2
C.symmetric_difference_update(B)
print("   C.symmetric_difference_update(D) = {}".format(C))
D.symmetric_difference_update(A)
print("   D.symmetric_difference_update(A) = {}\n".format(D))

C = {0,1,2,3,4,5,6,7,8,9}
D = {0,1,2,3,4,5,6,7,8,9}
print("[>]var1.isdisjoint(var2)")   #return boolean
print("   Apakah himpunan A dan C tidak meiliki irisan? ({})".format(A.isdisjoint(C)))
print("   Apakah himpunan A dan B tidak meiliki irisan? ({})\n".format(A.isdisjoint(B)))

C = {33,17,23}
D = {10,11,32}
print("[>]var1.issubset(var2)") #return boolean
print("   Apakah himpunan C adalah subset dari A? ({})".format(C.issubset(A)))
print("   Apakah himpunan C adalah subset dari B? ({})".format(C.issubset(B)))
print("   Apakah himpunan D adalah subset dari B? ({})".format(D.issubset(B)))
print("   Apakah himpunan D adalah subset dari A? ({})\n".format(D.issubset(A)))

C = {33,17,23}
D = {10,11,32}
print("[>]var1.issuperset(var2)") #return boolean
print("   Apakah himpunan A adalah superset dari C? ({})".format(A.issuperset(C)))
print("   Apakah himpunan B adalah superset dari C? ({})".format(B.issuperset(C)))
print("   Apakah himpunan B adalah superset dari D? ({})".format(B.issuperset(D)))
print("   Apakah himpunan A adalah superset dari D? ({})\n".format(A.issuperset(D)))

print(120*"=")