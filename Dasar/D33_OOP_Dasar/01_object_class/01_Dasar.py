#Deklarasi class mahasiswa yang berisi kosong
class mahasiswa :
    nim = "NIM Mahasiswa"       #Variable Class
    nama = "Nama Mahasiswa"     #Variable Class

#Membuat objek dari class yang sudah dibuat
mahasiswa1 = mahasiswa()
mahasiswa2 = mahasiswa()

print(50*"=")
print(mahasiswa)
print(mahasiswa.nim)
print(mahasiswa.nama)
print()
print(mahasiswa1)
print(mahasiswa1.nim)
print(mahasiswa1.nama)
print()
print(mahasiswa2)
print(mahasiswa2.nim)
print(mahasiswa2.nama)

#Merubah nilai dari attribut pada masing" object yang telah terbuat
mahasiswa1.nim = "1803015106"
mahasiswa1.nama = "Rangga Wiraguna"
mahasiswa2.nim = "1803015057"
mahasiswa2.nama = "Fasya Nazihah"

print(50*"=")
print(mahasiswa)
print(mahasiswa.nim)
print(mahasiswa.nama)
print()
print(mahasiswa1)
print(mahasiswa1.nim)
print(mahasiswa1.nama)
print()
print(mahasiswa2)
print(mahasiswa2.nim)
print(mahasiswa2.nama)

#Menambahkan attribut baru dari masing" object yang telah terbuat
mahasiswa1.alamat = "Jakarta"
mahasiswa2.alamat = "Cileungsi"

print(50*"=")
print(mahasiswa)
print(mahasiswa.nim)
print(mahasiswa.nama)
print()
print(mahasiswa1)
print(mahasiswa1.nim)
print(mahasiswa1.nama)
print(mahasiswa1.alamat)
print()
print(mahasiswa2)
print(mahasiswa2.nim)
print(mahasiswa2.nama)
print(mahasiswa2.alamat)

print(50*"=")