#Untuk dapat mengoperasikan queue pada file ini kita harus melakukan import modul deque
#walaupun pada modul LQueue sudah terdapat import deque
from collections import deque as queue

#Melakukan import modul sekaligus, blok main pada modul tidak akan dieksekusi karena __name__ akan berubah menjadi nama file yang menjalankan program
from D23_C_strukturData import SStack,LQueue

print(50*"=")
data1 = list()

SStack.masuk(data1, 10)
print("Tampilan stack : " + str(data1) + "\n")

SStack.masuk(data1, (20, 30))
print("Tampilan stack : " + str(data1) + "\n")

SStack.keluar(data1)
print("Tampilan stack : " + str(data1) + "\n")

SStack.masuk(data1, 30)
print("Tampilan stack : " + str(data1) + "\n")

SStack.masuk(data1, (40, 50, 60))
print("Tampilan stack : " + str(data1) + "\n")

SStack.keluar(data1)
print("Tampilan stack : " + str(data1) + "\n")

SStack.reset(data1)
print("Tampilan stack : " + str(data1) + "\n")
print(50*"=")

print(50*"=")
data2 = queue()

LQueue.masuk(data2, 10)
print("Tampilan queue : " + str(data2)[6:(len(str(data2))-1)] + "\n")

LQueue.masuk(data2, (20, 30))
print("Tampilan queue : " + str(data2)[6:(len(str(data2))-1)] + "\n")

LQueue.keluar(data2)
print("Tampilan queue : " + str(data2)[6:(len(str(data2))-1)] + "\n")

LQueue.masuk(data2, 40)
print("Tampilan queue : " + str(data2)[6:(len(str(data2))-1)] + "\n")

LQueue.masuk(data2, (50,60))
print("Tampilan queue : " + str(data2)[6:(len(str(data2))-1)] + "\n")

LQueue.keluar(data2)
print("Tampilan queue : " + str(data2)[6:(len(str(data2))-1)] + "\n")

LQueue.reset(data2)
print("Tampilan queue : " + str(data2)[6:(len(str(data2))-1)] + "\n")
print(50*"=")
