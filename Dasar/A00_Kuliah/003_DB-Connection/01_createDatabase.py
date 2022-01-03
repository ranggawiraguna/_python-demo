import pymysql

db = pymysql.connect("localhost","root","")
cursor = db.cursor()

sql = "CREATE DATABASE koneksi"

try :
    cursor.execute(sql)

except :
    cursor.execute("DROP DATABASE IF EXISTS koneksi")
    cursor.execute(sql)

finally :
    cursor.execute("SELECT VERSION()")
    desc = cursor.fetchone()
    print("[!]Database koneksi telah dibuat!")
    print("[!]Database Version : {}".format(desc))
    print("[!]Deskripsi Databases : ")

    cursor.execute("SHOW DATABASES")
    desc = cursor.fetchall()

    nomor = 1
    for row in desc :
        for column in row :
            print("   {}. {}".format(nomor, column))
        nomor += 1

    db.close()
