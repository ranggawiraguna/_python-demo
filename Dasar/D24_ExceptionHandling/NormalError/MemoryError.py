try :
    print("Gunakan penyimpanan memori sesuai kapasitas!")

except MemoryError as e :
    print()
    print("[!]Error Message\t\t: Memory kehabisan untuk menyimpan data!")
    print("[!]Type Error\t\t\t: {}".format(str(type(e))[8:(len(str(type(e))) - 2)]))
    print("[!]Detail Error\t\t\t: {}!".format(e))

else :
    print()
    print("[!]Data telah tersimpan dalam memori!")

finally :
    print()
    print("[!]Blok try-except berhasil digunakan!")
