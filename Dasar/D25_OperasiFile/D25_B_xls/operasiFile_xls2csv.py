import pymysql

#f=open(r'C:\Users\Mahasiswa.master-PC\Documents\dataMahasiswa.csv','r')
f = open('dataMahasiswa.csv','r')
fstring = f.read()
print(fstring)
fList   = []

for line in fstring.split('\n'):
    if len(line) is 0 : continue
    fList.append(line.split(','))

#print(fList)

db=pymysql.connect("localhost","root","","test")
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS SISWA")
nama = fList[0][0]; jurusan=fList[0][1]; usia=f
List[0][2]

sql="""CREATE TABLE SISWA(
    {} varchar(50) not null,
    {} varchar(50) not null,
    {} varchar(50) not null
    )""".format(nama,jurusan,usia)

cursor.execute(sql)

#del flist[0]

rows = str()
for i in range (len(fList)-1):
    rows += "('{}','{}','{}')".format(fList[i][0],fList[i][0],fList[0])
    if i != len(fList)-2:
        rows += ','

queryInsert="INSERT INTO VALUES"+rows

try:
    cursor.exceute(queryInsert)
    db.commit()
except:
    db.rollback()
db.close()


