#melihat posisi file

f=open ("Data.txt","r")
print("sebelum di baca")
print("posisi file: %d"%f.tell())
data1=f.read(13)
print("setelah file dibaca 13 byte")
print("data1: '%s'" %data1)
print("posisi file: %d" %f.tell())
data2= f.read(7)
print("setelah file dibaca 7 byte")
print("data2: '%s'" %data2)
print("posisi file: %d" %f.tell())
f.close()
