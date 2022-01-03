#Mengimport package dengan mengaliaskan sebagai operasi
#karena package terdapat __init__ yang telah mengimpor setiap keseluruhan modulnya, jadi file ini dapat langsung mengoperasikan
#semua isi modul yang telah di import pada init

import  D23_B_mahasiswa as operasi

data = list()
dataMHS = list()

data.append(operasi.inputBiodata())
print()
data.append(operasi.inputNilai(int(input("Masukkan Banyak Mata Kuliah : "))))

dataMHS.append(data)

print(50*"=")

operasi.tampilkanBiodata(dataMHS, len(dataMHS))
print()
operasi.tampilkanSemuaNilai(dataMHS)

