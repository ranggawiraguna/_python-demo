try :
    data = float(input("[>]Masukkan angka dibawah 100\t: "))

    assert (data < 100), data     # assert (kondisi benar), argumen ketika salah

except AssertionError as e :
    print()
    print("[!]Error Message\t\t: Masukkan input dengan benar!")
    print("[!]Type Error\t\t\t: {}".format(str(type(e))[8:(len(str(type(e))) - 2)]))
    print("[!]Detail Error\t\t\t: {} bernilai >= 100".format(e))

else :
    print()
    print("[!]Data yang dimasukkan sesuai ketentuan!")

finally :
    print()
    print("[!]Blok try-except berhasil digunakan!")