# Generator Expression = ()
# Membuat generator object sederahana yang berfungsi sebagai iterable

from decimal import  Decimal as dec

dataList = [90, 98, 95, 95, 70, 100, 100, 82, 98, 100, 87]
generator1 = (("{:.2f}%".format(dec(str(x))*dec('0.3'))) for x in dataList)

print(50 * '=')
print(type(generator1))
print("[0]  ", dataList[0], " >>", next(generator1))
print("[1]  ", dataList[1], " >>", next(generator1))
print("[2]  ", dataList[2], " >>", next(generator1))
print("[3]  ", dataList[3], " >>", next(generator1))
print("[4]  ", dataList[4], " >>", next(generator1))
print("[5]  ", dataList[5], ">>", next(generator1))
print("[6]  ", dataList[6], ">>", next(generator1))
print("[7]  ", dataList[7], " >>", next(generator1))
print("[8]  ", dataList[8], " >>", next(generator1))
print("[9]  ", dataList[9], ">>", next(generator1))
print("[10] ", dataList[10], " >>", next(generator1))
print(50 * '=')


dataList = [90, 98, 95, 95, 70, 100, 100, 82, 98, 100, 87]
generator2 = (("{:.2f}%".format(dec(str(x))*dec('0.3'))) for x in dataList)

print(50 * '=')
index = 0
for item in generator2 :
    print("[",index, "] ", dataList[index], " >> ", item, sep='')
    index += 1
print(50 * '=')

#Beberapa built-in function yang bisa menggunakan generator expression
dataList = [90, 98, 95, 95, 70, 100, 100, 82, 98, 100, 87]

print(50 * '=')
print("Nilai Terbesar     =", max(x for x in dataList))
print("Jumlah Total Nilai =", sum(x for x in dataList))
print("Rata-rata Nilai    = {:.2f}".format(dec(str(sum(x for x in dataList)))/dec(str(len(dataList)))))
print(50 * '=')

print(50 * '=')
generator3 = (x for x in dataList)
print("Nilai Terbesar     =", max(x for x in generator3))
generator3 = (x for x in dataList)
print("Jumlah Total Nilai =", sum(x for x in generator3))
generator3 = (x for x in dataList)
print("Rata-rata Nilai    = {:.2f}".format(dec(str(sum(x for x in generator3)))/dec(str(len(dataList)))))
print(50 * '=')


