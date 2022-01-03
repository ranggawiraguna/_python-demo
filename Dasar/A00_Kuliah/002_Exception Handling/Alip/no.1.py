print(50 * "=")
print("{:^50}".format("MENGHITUNG LUAS PERSEGI PANJANG"))
print((50 * "=") + "\n")
print(50 * "-")

keluar = 'y'
while (keluar == 'y') or (keluar == 'Y'):
    try :
        panjang = eval(input("Masukkan Panjang\t\t\t\t: "))
        lebar = float(input("Masukkan Lebar\t\t\t\t\t: "))

    except EOFError :
        print("\nMasukkan Input terlebih dahulu")

    except SyntaxError :
        print("\nMasukkan Input sesuai perintah!")

    except NameError :
        print("\nMasukkan Input dengan benar!")

    except ValueError :
        print("\nMasukkan Input berupa angka")

    else :
        luas = panjang * lebar
        print("Hasil Luas Persegi\t:", luas)

    print(50 * "-")
    keluar = input("Apakah ingin mengulang kembali?(y/t): ")
    print("\n")

print(50 * "=")