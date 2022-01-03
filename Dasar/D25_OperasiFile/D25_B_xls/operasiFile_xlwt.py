import xlwt

dataNim = ["1803015001","1803015002","1803015003","1803015004","1803015005"]
dataNama = ["Budi","Andi","Fasya","Nisa","Ratu"]
dataNilai = [89, 70, 80, 89, 77]

file = xlwt.Workbook()

sheet = file.add_sheet("Data Mahasiswa")

#Judul
sheet.write(0, 0, "NIM")
sheet.write(0, 1, "Nama")
sheet.write(0, 2, "Nilai")

row = 1
for x,y,z in zip(dataNim, dataNama, dataNilai) :
    sheet.write(row, 0, x)
    sheet.write(row, 1, y)
    sheet.write(row, 2, z)
    row += 1

file.save(r"E:\Rangga Wiraguna\Informatika\Files\dataMahasiswa.xls") #Save in directory sistem
file.save("dataMahasiswa.xls")  #Save in directory project