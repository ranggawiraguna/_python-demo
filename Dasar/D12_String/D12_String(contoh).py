#STRING


#String concate
print(50*"=")
print("STRING CONCATE")
kata = 'Rangga'
print("[>]kata == " + kata)
kata = kata + ' ' + 'Wiraguna'
print("[>]kata == " + kata)

#Mengakses setiap karakter string
print(50*"=")
print("STRING INDEKS")
print("[>]kata[0] == " + kata[0])
print("[>]kata[8] == " + kata[7])

#Memeriksa anggota string
print(50*"=")
print("MEMERIKSA DATA STRING")
print("[>]Apakah 'W' ada dalam string? (" + str('W' in kata) + ")")
print("[>]Apakah 'gg' ada dalam string? (" + str('gg' in kata) + ")")
print("[>]Apakah 'Z' ada dalam string? (" + str('Z' in kata) + ")")
print()
print("[>]Apakah 'R' tidak ada dalam string? (" + str('R' not in kata) + ")")
print("[>]Apakah 'aa' tidak ada dalam string? (" + str('aa' not in kata) + ")")
print("[>]Apakah 'Y' tidak ada dalam string? (" + str('Y' not in kata) + ")")

#Memeriksa banyak anggota(karakter) pada string
print(50*"=")
print("STRING LENGHT")
print("[>]panjang kata == " + str(len(kata)) + "(karakter)")

#Karakter Escape
print(50*"=")
print("STRING(karakter escape)\n")
print("[>]Kutip tiga(''')\n   " + '''He said, "What's there"''')
print("[>]Escape chr(\')\n    " + 'He said, What\'s there"')
print("[>]Escape chr(\")\n    " + "He said, \"What's there\"")

#String Format

print(50*"=")
print("STRING Format(OLD)\n")
print("[>]Normal %\n   " + "%s = %s" % ('Nama', kata))
print("[>]Precision\n   " + "%f = %0.3f\n   %f = %0.3f" % (5/7, 5/7, 6/9, 6/9))
print("[>]Width&Posisi\n   " + "%-10s | %f | %10.2f" % ('5/7',5/7,5/7))

print("\n")
print("STRING Format(NEW)\n")
print("[>]Argumen Index\n   " + "{1} = {0}".format(kata, 'Nama'))
print("[>]Integer to Biner\n   " + "{0} = {0:b}\n   {1} = {1:b}".format(18, 26))
print("[>]Eksponensial\n   " + "{0} = {0:e}\n   {1} = {1:e}".format(18, 26))
print("[>]Precision\n   " + "{0} = {0:.3f}\n   {1} = {1:.3f}".format(5/7, 6/9))
print("[>]Width&Posisi\n   " + "{0:<10} | {1:^15f} | {1:>10.2f}".format('5/7',5/7))
print("[>]Padding\n   " + "{:05} | {:010} | {:015}".format(12, 345, 4567))
print("[>]Tanda(-+)\n   " + "{:+d} | {: d} | {:=5} | {:=+5}".format(20, -20, -20, 20))

dataDict = {'first':'Rangga', 'second':'Wiraguna', 'third':'Rudiyanto'}
print("[>]PlaceHolder\n   " + "{first} | {second} | {third}".format(**dataDict))
print("[>]PlaceHolder\n   " + "{first} | {second} | {third}".format(first='Rangga', second='Wiraguna', third='Rudiyanto'))

dataDict = {'first':'Rangga', 'second':'Wiraguna', 'third':'Rudiyanto'}
print("[>]GetItem & GetAttr\n   " + "{data[first]} | {data[second]} | {data[third]}".format(data=dataDict))

dataList = [90,98,95]
print("[>]GetItem & GetAttr\n   " + "{data[0]} | {data[1]} | {data[2]}".format(data=dataList))

class mahasiswa(object):
    biodata = {'nim':'1803015106', 'nama':'Rangga'}
    ips = [{'smt1':3.45}, {'smt2':3.39}, {'smt3':4.00}]
    ipk = 4.00
print("[>]GetItem & GetAttr\n   " + "{data.biodata[nim]} | {data.biodata[nama]} | {data.ipk}".format(data=mahasiswa()))
print("[>]GetItem & GetAttr\n   " + "{data.ips[0][smt1]} | {data.ips[1][smt2]} | {data.ips[2][smt3]}".format(data=mahasiswa()))

from datetime import datetime
print("[>]Datetime\n   " + "{:%Y-%m-%d ~ %H:%M}".format(datetime(2000, 6, 20, 18, 0)))

dt = datetime(2000, 6, 20, 18, 0)
print("[>]Datetime\n   " + "{:{date} ~ {time}}".format(dt, date='%Y-%m-%d', time='%H:%M'))

print("[>]Parameter\n   " + "|{:{align}{width}}|".format("Rangga Wiraguna", align='^', width='20'))
print("[>]Parameter\n   " + "| {:.{prec}} = {:.{prec}f} |".format("Value", 37.18293, prec=3))
print("[>]Parameter\n   " + "{:=+{width}.{prec}f}".format(37.18293, width=10, prec=3))

print("[>]KeyFormatSequence\n   " + "{:{}{}{}.{}{}}".format(37.18293, '=', '+', 10, 3, 'f' ))
print("[>]KeyFormatSequence\n   " + "|{:{}{}{}.{}{}}|".format(37.18293, '^','+', 15, 3, 'f' ))

print("[>]KeyFormatParameter\n   " + "|{:{}{}{width}.{prec}{}}|".format(37.182931, '=', '+', 'f', width=10, prec=3))

class mahasiswa(object) :
    def __format__(self, format_spec):
        if format_spec == "biodata" :
            return "1803015106 | Rangga Wiraguna"
        return "format yang dimasukkan salah"

print("[>]ObjectCustom\n   " + "{:biodata}".format(mahasiswa()))
print("[>]ObjectCustom\n   " + "{:nilai}".format(mahasiswa()))


#Method String
print(50*"=")
print("STRING Method\n")
teks1 = 'Informatika'
teks2 = 'Python'
teks3 = 'Fakultas Teknik Informatika'
print("[>]varstring.lower()\n   " + "{} >> {}".format(teks1,teks1.lower())) #Membuat semua karakter String menjadi huruf besar
print("   {} >> {}\n".format(teks2,teks2.lower()) )

print("[>]varstring.upper()\n   " + "{} >> {}".format(teks1,teks1.upper())) #Membuat semua karakter String menjadi huruf besar
print("   {} >> {}\n".format(teks2,teks2.upper()) )

print("[>]varstring.split()\n   " + "{}\n   {}\n".format(teks3,teks3.split())) #Membuat String menjadi data terpisah untuk setip kata yang disimpan sebagai list

print("[>]varstring.starswith()\n   " + "{} startswith('I')? ({})".format(teks1,teks1.startswith('I'))) #Memeriksa karakter awal pada String yang dilempar pada parameter
print("   {} startswith('Py')? ({})".format(teks2,teks2.startswith('Py')))
print("   {} startswith('Pyh')? ({})\n".format(teks2,teks2.startswith('Pyh')))

print("[>]varstring.endswith()\n   " + "{} endswith('a')? ({})".format(teks1,teks1.endswith('a')))     #Memeriksa karakter akhir pada String yang dilempar pada parameter
print("   {} endswith('on')? ({})".format(teks2,teks2.endswith('on')))
print("   {} endswith('ton')? ({})\n".format(teks2,teks2.endswith('ton')))

print("[>]varstring.join()\n   " + "{} >> {}".format(teks2,'-'.join(teks2))) #Menambahkan string pada setiap karakter(String), jika di list pada pemisah anggotanya
print("   {} >> {}".format(teks3,"-".join(["Fakultas", "Teknik", "Informatika"])))
print(50*"=")