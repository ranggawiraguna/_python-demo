print(50 * "=")
print("{:^50}".format("MENGHITUNG LUAS PERMUKAAN BALOK"))
print((50 * "=") + "\n")

keluar = 'y'
while (keluar == 'y') or (keluar == 'Y'):
    print(50 * "-")

    try :
        panjang = eval(input("Masukkan Panjang\t\t\t\t: "))
        lebar = float(input("Masukkan Lebar\t\t\t\t\t: "))
        tinggi = eval(input("Masukkan Tinggi\t\t\t\t\t: "))

    except EOFError :
        print("\nMasukkan Input terlebih dahulu")
        keluar = ' '

    except SyntaxError :
        print("\nMasukkan Input sesuai perintah!")

    except NameError :
        print("\nMasukkan Input dengan benar!")

    except ValueError :
        print("\nMasukkan Input berupa angka")

    else :
        luas = ((lebar * tinggi) * 2) + ((panjang * lebar) * 2) + \
                    ((panjang * tinggi) * 2)
        print("Hasil Luas Seluruh Permukaan\t:", luas)

    print(50 * "-")
    keluar = input("Apakah ingin mengulang kembali?(y/t): ")
    print("\n")

print(50 * "=")
