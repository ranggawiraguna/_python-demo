#Operasi File .txt

#Mode Pengoperasian
# 'r'  >> Mode membaca file .txt
# 'w'  >> Mode Menulis file .txt - bersifat overwrite(menimpa) jika terdapat nama file yang sama - jika file belum ada, maka akan dibuat file baru
# 'a'  >> Mode appending file .txt - Menambahkan teks pada akhir cursor pada file yang dibuka
# 'r+' >> Mode read and write file .txt - Dapat menulis sekaligus membaca file yang dibuka

#Mode write 'w'
file = open("Data.txt", 'w')
file.write("Nama\t : Rangga Wiraguna\nNIM \t : 1803015106\nJurusan\t : Teknik Informatika\n")
file.close()

#Mode read 'r'
print("file.read()")
file = open("Data.txt", 'r')
print(file.read())
file.close()

print("file.read(--n)")
file = open("Data.txt", 'r')
print('file.read(8)  >> "{}"'.format(file.read(8)))
print('file.read(15) >> "{}"'.format(file.read(15)))
file.close()
print()

print("file.readline()")
file = open("Data.txt", 'r')
print("[1]", file.readline(), end='')
print("[2]", file.readline(), end='')
print("[3]", file.readline(), end='')
file.close()
print()

print("file.readlines()")
file = open("Data.txt", 'r')
print(file.readlines(), end='')
file.close()
print("\n")

#Mode appending 'a'
print("file.write() >> 'a' >> append")
file = open("Data.txt", 'a')
file.write("Angkatan : 2018\n")
file.write("IPK \t : 3.42")
file.close()

file = open("Data.txt", 'r')
print(file.read())
file.close()
print()




