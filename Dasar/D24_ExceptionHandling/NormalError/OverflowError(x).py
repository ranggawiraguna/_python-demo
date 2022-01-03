try :
    #Statement yang menjalankan pengoperasian aritmatika terlalu besar


except OverflowError as e :
    print()
    print("[!]Error Message\t\t: Bilangan yang dioperasikan terlalu besar untuk direpresentasikan!")
    print("[!]Type Error\t\t\t: {}".format(str(type(e))[8:(len(str(type(e))) - 2)]))
    print("[!]Detail Error\t\t\t: {}".format(e))

else :
    print()
    print("[!]operasi aritmatika berhasil dijalankan")

finally :
    print()
    print("[!]Blok try-except berhasil digunakan!")

