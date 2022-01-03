import pymysql

db = pymysql.connect("localhost", "root", "", "koneksi")
cursor = db.cursor()

sql = """INSERT INTO mahasiswa(nim, nama, kelas, nilai)
         VALUES('%s', '%s', '%s', '%d')"""\
         % ('1803015106', 'Rangga Wiraguna', '3F', 50)

try:
    cursor.execute(sql)
    db.commit()

except:
    db.rollback()

else :
    print("[!]Table mahasiswa telah terbuat")
    print("[!]Deskripsi tabel : ")

    cursor.execute("SELECT * FROM mahasiswa")
    data = cursor.fetchall()

    print("   +" + (48 * "-") + "+  ")
    print("   {:<13}{:<18}{:<9}{:<9}|"
          "".format("| nim", "| nama", "| kelas", "| nilai"))
    print("   +" + (48 * "-") + "+  ")
    for row in data :
        print("   ",end='')
        for column in row :
            print("{:<8} ".format("| "+ str(column)), end='')
        print("|")
    print("   +" + (48 * "-") + "+  ")

    db.close()
