# List Comprehension
# [ varData(nilai disimpan kedalam list) - Looping(setiap nilaiIterable disimpan dalam varData) - Selection(memfilter nilaiIterable Looping) ]

#Menggunakan modul desimal untuk fungsi Decimal dengan nama dec >> berfungsi untuk melakukan perhitungan dengan hasil yang tepat
from decimal import Decimal as dec

print(150*'=')
dataList = [ x for x in range(20) ]
dataGanjil = [ x for x in dataList if ((x%2)==1) ]

print("[>]dataList    =", dataList)
print("[>]dataGanjil  =", dataGanjil)
print(150*'=')


print(150*'=')
dataList = [ x for x in range(20) ]
dataRatusan = [ (x*100) for x in dataList if ((x*100)>=100)]

print("[>]dataList    =", dataList)
print("[>]dataRatusan =", dataRatusan)
print(150*'=')


print(150*'=')
dataList = [ 0.2171, 0.3209, 0.3451, 0.5789, 0.7898, 1.2912, 1.5123, 1.7892 ]
dataPersen = [ ("{:.2f}".format((dec(str(x)) * dec('100'))) + '%')  for x in dataList if (x<1) ]

print("[>]dataList    =", dataList)
print("[>]dataPersen  =", dataPersen)
print(150*'=')