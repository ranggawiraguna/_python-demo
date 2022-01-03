try :
    import aplikasi

except ImportError as e :
    print()
    print("[!]Error Message\t\t: Modul yang di import tidak tersedia!")
    print("[!]Type Error\t\t\t: {}".format(str(type(e))[8:(len(str(type(e))) - 2)]))
    print("[!]Detail Error\t\t\t: {}".format(e))

else :
    print()
    print("[!]Modul berhasil di import ke dalam file")

finally :
    print()
    print("[!]Blok try-except berhasil digunakan!")
