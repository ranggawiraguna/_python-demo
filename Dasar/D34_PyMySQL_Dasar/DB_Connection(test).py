import pymysql

try :
    db = pymysql.connect("localhost", "root", "")

except pymysql.err.OperationalError :
    print(90*"=")
    print("Aktifkan fitur MySQL & Apache pada XAMPP untuk menggunakan Database!")
    print(90*"=")
    exit(0)

else :
    cursor = db.cursor()

    try :
        cursor.execute("USE dataMahasiswa")
        cursor.execute("show tables")
        tables = cursor.fetchone()
        if type(tables) is type(tuple()) :
            if "biodata" not in  tables :
                raise NameError

        else :
            raise NameError

    except NameError :
        cursor.execute("CREATE TABLE biodata(nim CHAR(10) PRIMARY KEY NOT NULL,"
                                            "nama CHAR(30) NOT NULL,"
                                            "alamat CHAR(100) NOT NULL,"
                                            "jurusan CHAR(20) NOT NULL)")

    except pymysql.err.InternalError :
        cursor.execute("CREATE DATABASE dataMahasiswa")
        cursor.execute("USE dataMahasiswa")
        cursor.execute("CREATE TABLE biodata(nim CHAR(10) PRIMARY KEY NOT NULL,"
                                            "nama CHAR(30) NOT NULL,"
                                            "alamat CHAR(100) NOT NULL,"
                                            "jurusan CHAR(20) NOT NULL)")

    db.commit()
    db.close()


if __name__ == '__main__' :

    print(90*"=")
    print("{:^90}".format("PROGRAM CRUD BIODATA MAHASISWA"))
    print(90*"=")

    while(True) :
        db = pymysql.connect("localhost", "root", "", "dataMahasiswa")
        cursor = db.cursor()

        print(90*"-")
        print("Pilihan : [1]Tampilkan Semua Biodata\n"
              "          [2]Cari Biodata Mahasiswa\n"
              "          [3]Input Biodata Mahasiswa\n"
              "          [4]Hapus Biodata Mahasiswa\n"
              "          [5]Reset Data Biodata\n"
              "          [0]Keluar Program")
        pilihan = input("Pilih\t:  ")
        print(90*"-")

        print(90*"-")
        if pilihan is '0' :
            print("Program telah dihentikan!")
            print(90 * "-")
            break

        elif pilihan is '1' :
            cursor.execute("SELECT * FROM biodata")
            data = cursor.fetchall()
            describe = "+" + (87 * "-") + "+\n" + \
                       "{:<16}{:<24}{:<24}{:<24}|\n".format("| NIM", "| Nama", "| Alamat", "| Jurusan") + \
                       "+" + (87 * "-") + "+\n"

            if len(data) is 0 :
                describe = describe + "| Empty set in table\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|\n"

            else :
                for row in data:
                    size = 16
                    for column in row :
                        space = ((size - (len(column)+3))//4) + 1
                        describe = describe + "{}".format("| " + str(column)) + ("\t"*space)
                        size = 24
                    describe = describe + "|" + "\n"

            describe = describe + "+" + (87 * "-") + "+"

            print(describe)

        elif pilihan is '2' :
            key = input("[!]Masukkan PrimaryKey(NIM) mahasiswa : ")
            cursor.execute("SELECT * FROM biodata WHERE nim='{}'".format(key))

            data = cursor.fetchone()
            describe = "+" + (87 * "-") + "+\n" + \
                       "{:<16}{:<24}{:<24}{:<24}|\n".format("| NIM", "| Nama", "| Alamat", "| Jurusan") + \
                       "+" + (87 * "-") + "+\n"

            if (type(data) is not type(tuple())) :
                describe = describe + "| Unknown data in table\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|\n"

            else :
                size = 16
                for column in data:
                    space = ((size - (len(column) + 3)) // 4) + 1
                    describe = describe + "{}".format("| " + str(column)) + ("\t" * space)
                    size = 24
                describe = describe + "|\n"

            describe = describe + "+" + (87 * "-") + "+"

            print(describe)

        elif pilihan is '3' :
            nim = input("[>]Masukkan NIM\t\t: ")
            if len(nim)>10 : nim = nim[:10]

            nama = input("[>]Masukkan Nama\t: ")
            if len(nama)>30 : nama = nama[:30]

            alamat = input("[>]Masukkan Alamat\t: ")
            if len(alamat)>30 : alamat = alamat[:30]

            jurusan = input("[>]Masukkan Jurusan\t: ")
            if len(jurusan)>30 : jurusan = jurusan[:30]

            try :
                cursor.execute("INSERT INTO biodata VALUES('%s', '%s', '%s','%s')"%(nim,nama,alamat,jurusan))

            except pymysql.err.IntegrityError :
                print("\n[!]IntegrityError\t: Duplicate entry '1803015106' for key 'PRIMARY'")

            cursor.execute("SELECT * FROM biodata WHERE nim='{}'".format(nim[:10]))

            data = cursor.fetchone()
            describe = "+" + (87 * "-") + "+\n" + \
                       "{:<16}{:<24}{:<24}{:<24}|\n".format("| NIM", "| Nama", "| Alamat", "| Jurusan") + \
                       "+" + (87 * "-") + "+\n"

            size = 16
            for column in data:
                space = ((size - (len(column) + 3)) // 4) + 1
                describe = describe + "{}".format("| " + str(column)) + ("\t" * space)
                size = 24
            describe = describe + "|" + "\n"

            describe = describe + "+" + (87 * "-") + "+"
            print(describe)

        elif pilihan is '4' :
            #Mengambil PrimaryKey record yang ingin di delete
            key = input("[!]Masukkan PrimaryKey(NIM) mahasiswa : ")

            #Mengambil record yang ingin di delete
            cursor.execute("SELECT * FROM biodata WHERE nim='{}'".format(key))

            data = cursor.fetchone()
            describe = "+" + (87 * "-") + "+\n" + \
                       "{:<16}{:<24}{:<24}{:<24}|\n".format("| NIM", "| Nama", "| Alamat", "| Jurusan") + \
                       "+" + (87 * "-") + "+\n"

            if (type(data) is not type(tuple())) :
                describe = describe + "| Unknown data in table\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|\n"

            else :
                size = 16
                for column in data:
                    space = ((size - (len(column) + 3)) // 4) + 1
                    describe = describe + "{}".format("| " + str(column)) + ("\t" * space)
                    size = 24
                describe = describe + "|\n"

            describeDelete = describe + "+" + (87 * "-") + "+"

            #Menghapus record yang ingin di delete
            cursor.execute("DELETE FROM biodata WHERE nim='{}'".format(key))

            #Menampilkan semua record setelah proses delete
            cursor.execute("SELECT * FROM biodata")
            data = cursor.fetchall()
            describe = "+" + (87 * "-") + "+\n" + \
                       "{:<16}{:<24}{:<24}{:<24}|\n".format("| NIM", "| Nama", "| Alamat", "| Jurusan") + \
                       "+" + (87 * "-") + "+\n"

            if len(data) is 0 :
                describe = describe + "| Empty set in table\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|\n"

            else :
                for row in data:
                    size = 16
                    for column in row:
                        space = ((size - (len(column) + 3)) // 4) + 1
                        describe = describe + "{}".format("| " + str(column)) + ("\t" * space)
                        size = 24
                    describe = describe + "|\n"

            describe = describe + "+" + (87 * "-") + "+"

            print("[>]Tampilan data terbaru : ")
            print(describe)
            print()

            #Menampilkan record yang di delete
            print("[>]Data Yang dihapus :")
            print(describeDelete)

        elif pilihan is '5' :
            cursor.execute("TRUNCATE biodata")
            print("Tabel Biodata telah dikosongkan!")

        else :
            print("Pilihan yang dimasukkan salah!")

        print(90 * "-")
        print("\n")
        db.commit()
        db.close()

    print(90*"=")
