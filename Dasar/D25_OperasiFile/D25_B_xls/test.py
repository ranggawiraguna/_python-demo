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

    print("dataMahasiswa :", dataMahasiswa)
    print("data :", data)

    dataMahasiswa.append(data)
    print("dataMahasiswa :", dataMahasiswa)
    input()


print(dataMahasiswa[0]['Nama'])