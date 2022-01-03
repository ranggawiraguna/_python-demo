dataList = [0,10,20,30,40]  #indeks = [0,1,2,3,4]

try :
    print("Nilai :", dataList[5])

except IndexError as e :
    print()
    print("[!]Error Message\t\t: Index yang dipanggil pada variable list tidak tersedia!")
    print("[!]Type Error\t\t\t: {}".format(str(type(e))[8:(len(str(type(e))) - 2)]))
    print("[!]Detail Error\t\t\t: {}".format(e))

else :
    print()
    print("[!]Pemanggilan dataList berhasil")

finally :
    print()
    print("[!]Blok try-except berhasil digunakan!")

