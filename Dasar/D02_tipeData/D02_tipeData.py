##TipeData


print(50*"=")
print("Integer(int)")
angkaInt = 378          #int(value)
print("Nilai Variabel\t\t: " + str(angkaInt))
print("Tipedata Variable\t: " + str(type(angkaInt)))

print(50*"=")
print("Float(float)")
angkaFloat = 253.81     #float(value)
print("Nilai Variabel\t\t: " + str(angkaFloat))
print("Tipedata Variable\t: " + str(type(angkaFloat)))

print(50*"=")
print("Boolean(bool)")      #Tipedata yang dapat menyimpan nilai logika true/false || 0/1
nilaiLogika = True          #bool(value)
print("Nilai Variabel\t\t: " + str(nilaiLogika))
print("Tipedata Variable\t: " + str(type(nilaiLogika)))

print(50*"=")
print("String(str)")        #Tipedata yang dapat menyimpan data berjenis karakter satu atau lebih
kata = "RANGGA"             #str(value)
print("Nilai Variabel\t\t: " + kata)
print("Nilai Variable[0]\t: " + kata[0])
print("Nilai Variable[1]\t: " + kata[1])
print("Nilai Variable[2]\t: " + kata[2])
print("Nilai Variable[3]\t: " + kata[3])
print("Nilai Variable[4]\t: " + kata[4])
print("Nilai Variable[5]\t: " + kata[5])
print("Tipedata Variable\t: " + str(type(kata)))


#String, array

print(50*"=")
print("List(list)")     #Kumpulan data yang bersifat mutable(isinya dapat dirubah)
data = ["Rangga", 20, "Juni", 2000]
print("Nilai Variabel\t\t: " + str(data))
print("Nilai Variable[0]\t: " + str(data[0]))
print("Nilai Variable[1]\t: " + str(data[1]))
print("Nilai Variable[2]\t: " + str(data[2]))
print("Nilai Variable[3]\t: " + str(data[3]))
print("Tipedata Variable\t: " + str(type(data)))


print(50*"=")
print("Tuple(tuple)")   #Kumpulan data yang bersifat immutable(isinya tidak dapat dirubah)
data2 = ("Rangga", 20, "Juni", 2000)
print("Nilai Variabel\t\t: " + str(data2))
print("Nilai Variable[0]\t: " + str(data2[0]))
print("Nilai Variable[1]\t: " + str(data2[1]))
print("Nilai Variable[2]\t: " + str(data2[2]))
print("Nilai Variable[3]\t: " + str(data2[3]))
print("Tipedata Variable\t: " + str(type(data2)))

print(50*"=")
print("Set(set)")   #Kumpulan data yang bersifat himpunan, tidak memiliki indeks pada elemennya
data3 = {60, 78, 88, 72, 78, 90, 88, 64}
print("Nilai Variabel\t\t: " + str(data3))
print("Tipedata Variable\t: " + str(type(data3)))

print(50*"=")
print("Dictionary(dict)")     #Kumpulan data yang bersifat mutable(isinya dapat dirubah)
data4 = {"nama":"Rangga", "tgl":20, "bulan":"Juni", "tahun":2000}
print("Nilai Variabel\t\t\t: " + str(data))
print('Nilai Variable["nama"]\t: ' + str(data4["nama"]))
print('Nilai Variable["tgl"]\t: ' + str(data4['tgl']))
print('Nilai Variable["bulan"]\t: ' + str(data4["bulan"]))
print('Nilai Variable["tahun"]\t: ' + str(data4["tahun"]))
print("Tipedata Variable\t\t: " + str(type(data4)))
print(50*"=")