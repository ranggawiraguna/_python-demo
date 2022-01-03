import pymysql

try :
    db = pymysql.connect("localhost", "root", "")

except pymysql.err.OperationalError :
    print(90*"=")
    print("Aktifkan fitur MySQL & Apache pada XAMPP untuk menggunakan Database!")
    print(90*"=")
    exit(0)

cursor = db.cursor()

cursor.execute("USE datamahasiswa")

cursor.execute("SELECT * FROM biodata")




