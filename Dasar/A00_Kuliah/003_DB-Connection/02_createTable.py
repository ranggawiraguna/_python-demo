import pymysql

db = pymysql.connect("localhost","root","","koneksi")
cursor = db.cursor()

sql = """CREATE TABLE mahasiswa(nim CHAR(10) PRIMARY KEY,
                                nama CHAR(50) NOT NULL,
                                kelas CHAR(5),
                                nilai INT(3)
                                )"""

try :
    cursor.execute(sql)
    db.commit()

except :
    db.rollback()

else :
    print("[!]Table mahasiswa telah terbuat")
    print("[!]Deskripsi tabel : ")
    cursor.execute("DESC mahasiswa")
    desc = cursor.fetchall()
    print("   +" + (65 * "-") + "+  ")
    print("   {:<11}{:<11}{:<11}{:<11}{:<11}{:<11}|".format
         ("| Field","| Type","| Null","| Key","| Default","| Extra"))
    print("   +" + (65 * "-") + "+  ")
    for row in desc :
        print("   ",end='')
        for column in row :
            print("{:<11}".format("| "+ str(column)), end='')
        print("|")
    print("   +" + (65 * "-") + "+  ")

    db.close()
