
print(50*"=")
angkaInt = int(input("[?]Masukkan data angka bilangan bulat : "))
print("[>]Angka yang anda masukkan adalah " + str(angkaInt))
print(50*"=")
angkaFloat = float(input("[?]Masukkan data angka bilangan real : "))
print("[>]Angka yang anda masukkan adalah " + str(angkaFloat))

print(50*"=")
teks = input("[?]Masukkan data teks : ")
print("[>]Teks yang anda masukkan adalah " + teks)

print(50*"=")
dataList = []
dataList.append(input("[?]Masukkan anggota list[0] : "))
dataList.append(input("[?]Masukkan anggota list[1] : "))
dataList.append(input("[?]Masukkan anggota list[2] : "))
print("[>]List yang anda buat adalah " + str(dataList))

print(50*"=")
buffer1 = input("[?]Masukkan anggota tetap tuple[0] : ")
buffer2 = input("[?]Masukkan anggota tetap tuple[1] : ")
buffer3 = input("[?]Masukkan anggota tetap tuple[2] : ")
dataTuple = (buffer1,buffer2,buffer3)
print("[>]List yang anda buat adalah " + str(dataTuple))

print(50*"=")
buffer1 = input("[?]Masukkan anggota set : ")
buffer2 = input("[?]Masukkan anggota set : ")
buffer3 = input("[?]Masukkan anggota set : ")
dataDict = {'satu':buffer1, 'dua':buffer2, 'tiga':buffer3}
print("[>]List yang anda buat adalah " + str(dataDict))
print(50*"=")


