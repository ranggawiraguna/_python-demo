try :
    print("Masukkan data dan jangan tekan ctrl+C untuk melakukan interrupsi!")
    data = input("[>]Masukkan data\t\t: ")

except EOFError as e :
    print()
    print("[!]Error Message\t\t: Jangan melakukan tombol interrupsi pada saat input data!")
    print("[!]Type Error\t\t\t: {}".format(str(type(e))[8:(len(str(type(e))) - 2)]))
    print("[!]Detail Error\t\t\t: {}!".format(e))

else :
    print()
    print("[!]Data berhasil ter-input kedalam sistem!")

finally :
    print()
    print("[!]Blok try-except berhasil digunakan!")
