dataDict = {'nama' : 'Rangga',
            'nim' : '1803015106',
            'jurusan' : 'Teknik Informatika',
            'angkatan' : '2018'
            }

try :
    print("Data :", dataDict['nilai'])

except KeyError as e :
    print()
    print("[!]Error Message\t\t: Key yang dipanggil tidak tersedia pada dictionary")
    print("[!]Type Error\t\t\t: {}".format(str(type(e))[8:(len(str(type(e))) - 2)]))
    print("[!]Detail Error\t\t\t: {}".format(e))

else :
    print()
    print("[!]Pemanggilan dataDict berhasil")

finally :
    print()
    print("[!]Blok try-except berhasil digunakan!")

