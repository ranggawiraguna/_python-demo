import xlrd

#Open file .xls in project
dataMahasiswa = list()

file = xlrd.open_workbook("dataMahasiswa.xls")
sheet = file.sheet_by_index(0)
banyakData = sheet.nrows

for baris in range(1, banyakData):
    data = dict()
    data[sheet.cell_value(rowx=0, colx=0)] = sheet.cell_value(rowx=baris, colx=0)
    data[sheet.cell_value(rowx=0, colx=1)] = sheet.cell_value(rowx=baris, colx=1)
    data[sheet.cell_value(rowx=0, colx=2)] = sheet.cell_value(rowx=baris, colx=2)
    dataMahasiswa.append(data)

print(100*'=')
for item in dataMahasiswa :
    print(item)
print(100*'=')



#Open file .xls in directory system
dataMahasiswa = list()

file = xlrd.open_workbook(r"E:\Rangga Wiraguna\Informatika\Files\dataMahasiswa.xls")
sheet = file.sheet_by_index(0)
banyakData = sheet.nrows

for baris in range(1, banyakData):
    data = dict()
    data[sheet.cell_value(rowx=0, colx=0)] = sheet.cell_value(rowx=baris, colx=0)
    data[sheet.cell_value(rowx=0, colx=1)] = sheet.cell_value(rowx=baris, colx=1)
    data[sheet.cell_value(rowx=0, colx=2)] = sheet.cell_value(rowx=baris, colx=2)
    dataMahasiswa.append(data)

print(100*'=')
for item in dataMahasiswa :
    print(item)
print(100*'=')