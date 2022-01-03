try :
    print(data)

except EOFError as e :
    print()
    print("[!]Error Message\t\t: Variable yang dicari tidak ada dalam sistem!")
    print("[!]Type Error\t\t\t: {}".format(str(type(e))[8:(len(str(type(e))) - 2)]))
    print("[!]Detail Error\t\t\t: {}!".format(e))

else :
    print()
    print("[!]Variable yang dicari ditemukan dalam sistem")

finally :
    print()
    print("[!]Blok try-except berhasil digunakan!")
