#DICTIONARY

#Deklarasi dictionary
data1 = {1:"Aqidah", 2:"Inggris", 3:"ISBD", 4:"Kalkulus", 5:"Muamalah", 6:"Matdis", 7:"Sisdig", 8:"SI", 9:"Strukdat", 10:"Prak.Strukdat"}
data2 = {"aqidah":86, "inggris":81, "isbd":76, "kalkulus":56, "muamalah":81, "matdis":92, "sisdig":82, "si":78, "sd":76, "psd":69}
data3 = {"biodata" : ["Rangga", "1803015106", "Teknik Informatika"],
         "nilai1" : (86,81,76,56,81,92,82,78,76,69)}
data4 = dict([('A',4),('B',3),('C',2),('D',1),('E',0)])
buffer = dict()

#Mengakses data dalam dictionary
print(200*"=")
print("MENGAKSES DICTIONARY\n")
print("[>]Manual varDict[key]")    #error runtime jika key tidak ada
print("   data1[6]                :", data1[6], type(data1[6]))
print('   data2["matdis"]         :', data2["matdis"], type(data2["matdis"]))
print('   data3["biodata"]        :', data3["biodata"], type(data3["biodata"]))
print('   data3["biodata"][2]     :', data3["biodata"][2])
print('   data4["A"]              :', data4['A'], type(data4['A']))
print()
print("[>]Fungsi varDict.get(key)")    #return value dari key, jika key tidak ada return None
print("   data1.get(6)            :", data1.get(6), type(data1.get(6)))
print('   data2.get("matdis")     :', data2.get("matdis"), type(data2.get("matdis")))
print('   data3.get("biodata")    :', data3.get("biodata"), type(data3.get("biodata")))
print('   data3.get("biodata")[2] :', data3.get("biodata")[2])
print('   data4.get("A")          :', data4.get('A'), type(data4.get('A')))
print('   data1.get(0)            :', data1.get(0), type(data1.get(0)))
print()
print("[>]Fungsi varDict.get(key,value)")    #return value dari key, jika key tidak ada return value argumen
print("   data1.get(6,v)            :", data1.get(6,"Data Tidak Ditemukan"), type(data1.get(6,"Data Tidak Ditemukan")))
print('   data2.get("matdis",v)     :', data2.get("matdis","Data Tidak Ditemukan"), type(data2.get("matdis","Data Tidak Ditemukan")))
print('   data3.get("biodata",v)    :', data3.get("biodata","Data Tidak Ditemukan"), type(data3.get("biodata","Data Tidak Ditemukan")))
print('   data3.get("biodata",v)[2] :', data3.get("biodata")[2])
print('   data4.get("A")          :', data4.get('A',"Data Tidak Ditemukan"), type(data4.get('A',"Data Tidak Ditemukan")))
print('   data1.get(0)            :', data1.get(0,"Data Tidak Ditemukan"), type(data1.get(0,"Data Tidak Ditemukan")))
print()

#Mengubah anggota dictionary
print(200*"=")
print("MENGUBAH ISI DICTIONARY\n")

print("[>]data1(before) :", data1, type(data1))
data1[1] = "Agama"                  #Merubah isi dari key yang ditentukan
print("   data1(after)  :", data1, type(data1))
print()
print("[>]data2(before) :", data2, type(data2))
data2["kalkulus"] = 90              #Merubah isi dari key yang ditentukan
print("   data2(after)  :", data2, type(data2))
print()
print("[>]data1(before) :", data1, type(data1))
data1[11] = "Kriptografi"           #Merubah isi dari key yang ditentukan, bila key tidak ada maka akan menambahkannya sebagai key baru
print("   data1(after)  :", data1, type(data1))
print()
print("[>]data2(before) :", data2, type(data2))
data2["kriptografi"] = 77           #Merubah isi dari key yang ditentukan, bila key tidak ada maka akan menambahkannya sebagai key baru
print("   data2(after)  :", data2, type(data2))
print()

#Menghapus anggota dictionary
print(200*"=")
print("MENGHAPUS ISI DICTIONARY\n")

print("[>]varDict.pop(key)")          #return value yang dihapus
print("   data1(before) :", data1, type(data1))
hapus = data1.pop(4)                  #Menghapus isi dari key yang ditentukan, error jika key tidak ditemukan
print("   data1(after)  :", data1, type(data1))
print("   Data dihapus  :", hapus, type(hapus))
print()
print("[>]varDict.pop(key,d)")        #return value yang dihapus
print("   data1(before) :", data1, type(data1))
hapus = data1.pop(0,"Data tidak ditemukan")   #Menghapus isi dari key yang ditentukan, mengembalikan nilai d jika key tidak ditemukan
print("   data1(after)  :", data1, type(data1))
print("   Data dihapus  :", hapus, type(hapus))
print()
print("[>]varDict.popitem()")          #return 1 item yang dihapus berjenis tuple secara acak
print("   data2(before) :", data2, type(data2))
hapus = data2.popitem()                #Menghapus isi dict secara acak, error jika dict kosong
print("   data2(after)  :", data2, type(data2))
print("   Data dihapus  :", hapus, type(hapus))
print()
print("[>]varDict.clear()")            #return none
print("   data4(before) :", data4, type(data4))
data4.clear()                          #Membersihkan isi dictionary menjadi kosong
print("   data4(after)  :", data4, type(data4))
print()
print("[>]del varDict")                #return none
print("   data4(before) :", data4, type(data4))
del data4                              #Menghapus variable
print("   data4(after)  : Data telah terhapus dari sistem")

#METHOD & FUNGSI LAIN UNTUK DICTIONARY
print(200*"=")
print("METHOD DAN FUNGSI LAIN UNTUK DICTIONARY\n")

print("[>]varDict.copy()")              #return new dict yang dicopy
data = data1.copy()
print("   data1 :", data1, type(data1))
print("   data  :", data, type(data))
print()
print("[>]varDict.keys()")              #return dict_keys dari varDict
dataKey = data1.keys()
print("   data1   :", data1, type(data1))
print("   dataKey :", dataKey, type(dataKey))
print()
print("[>]dict.fromkeys(varDict)")      #return new dict dengan kunci yang sama pada varDict dengan value None
data = dict.fromkeys(data1)
print("   data1  :", data1, type(data1))
print("   data   :", data, type(data))
print()
print("[>]dict.fromkeys(varDict,value)")      #return new dict dengan kunci yang sama pada varDict dengan value yang ditentukan
data = dict.fromkeys(data1,"Error")
print("   data1  :", data1, type(data1))
print("   data   :", data, type(data))
print()
print("[>]varDict.items()")             #return new dict dengan kunci yang sama pada varDict dengan value yang ditentukan
data = dict.fromkeys(data1,"Error")
print("   data1  :", data1, type(data1))
print("   data   :", data, type(data))
print()
print("[>]varDict.items()")              #return dict_item dari varDict
dataKey = data1.items()
print("   data1   :", data1, type(data1))
print("   dataKey :", dataKey, type(dataKey))
print()
print("[>]varDict.setdefault(key)")      #return value dari key yang ditentukan, jika key tidak ditemukan return None
data = data1.setdefault(1)
print("   data1  :", data1, type(data1))
print("   data   :", data, type(data))
print()
print("[>]varDict.setdefault(key,value)")      #return value dari key yang ditentukan, jika key tidak ditemukan return value argumen, dan dict key:value argumen dimasukkan dalam varDict
data = data1.setdefault(0,"Kunci Tidak Ditemukan")
print("   data1  :", data1, type(data1))
print("   data   :", data, type(data))
print()
print("[>]varDict1.update(dict)")           #return None, mengupdate varDict1 dengan ditambahkan isi dari dict, timpa jika terdapat kesamaan key
data = data1.copy()
data.update({0:"Ngopi"})
print("   data1  :", data1, type(data1))
print("   data   :", data, type(data))
print()
print("[>]varDict1.update(varDict2)")           #return None, mengupdate varDict1 dengan ditambahkan isi dari varDict2, timpa jika terdapat kesamaan key
data = data1.copy()
data.update(data2)
print("   data1  :", data1, type(data1))
print("   data   :", data, type(data))
print()
print("[>]varDict.values()")              #return dict_keys dari varDict
dataValues = data1.values()
print("   data1      :", data1, type(data1))
print("   dataValues :", dataValues, type(dataValues))
print()

print(200*"=")