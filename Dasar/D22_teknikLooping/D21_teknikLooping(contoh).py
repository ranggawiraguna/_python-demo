listKey = list(["Nim", "Nama", "Jurusan", "Angkatan"])
listInfo = tuple(["1803015106", "Rangga", "Teknik Informatika", "2018"])
dataSet = set(["Rangga", "Fasya", "Agung", "Alip", "Daffa", "Andre", "Alfaridzi"])
dataDict = dict([("Nim", "1803015106"),
                 ("Nama", "Rangga"),
                 ("Jurusan", "Teknik Informatika"),
                 ("Angkatan", "2018")
                ])

#Dasar Looping
print(100*"=")
index = 0
for data in listInfo :
    print("Index-{:<4}: {}".format(index,data))
    index += 1
print((100 * "=") + "\n\n")

#Enumerate Looping  //Menggunakan fungsi enumarate agar dapat menerima index looping otomatis yang dihasilkan oleh fungsi
print(100*"=")
for index,data in enumerate(listInfo) :
    print("Index-{:<4}: {}".format(index,data))
print((100 * "=") + "\n\n")

#zip Looping  //Menggunakan fungsi zip agar dapat menggabungkan 2-variable atau lebih sebagai iterable looping
print(100*"=")
for key,info in zip(listKey,listInfo) :
    print("{:<10}: {}".format(key,info))
print((100 * "=") + "\n\n")

#Set Looping  //Menggunakan variable set sebagai iterable looping
print(100*"=")

for data in dataSet :   #Variable set tidak memiliki index dan juga data didalam set di urutkan secara acak
    print("data  : {}".format(data))

print(100*"=")
for data in sorted(dataSet) :   #Mengurutkan isi set terlebih dahulu dengan metode urut per-karakter
    print("data  : {}".format(data))

print((100 * "=") + "\n\n")

#Dictionary Looping  //Menggunakan variable dict sebagai iterable looping
print(100*"=")

for data in dataDict.keys() :   #Variable set tidak memiliki index dan juga data didalam set di urutkan secara acak
    print("data  : {}".format(data))

print(100*"=")
for data in dataDict.values():   #Mengurutkan isi set terlebih dahulu dengan metode urut per-karakter
    print("data  : {}".format(data))

print(100*"=")
for data in dataDict.items():   #Mengurutkan isi set terlebih dahulu dengan metode urut per-karakter
    print("data  : {}".format(data))

print(100*"=")
for key,value in dataDict.items():   #Mengurutkan isi set terlebih dahulu dengan metode urut per-karakter
    print("{:<10}: {}".format(key,value))

print(100 * "=")

