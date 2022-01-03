print(50 * "=")
print("{:^50}".format("MENGHITUNG LUAS PERSEGI"))
print((50 * "=") + "\n")
print(50 * "-")

keluar = 'y'
while (keluar == 'y') or (keluar == 'Y'):
    try :
        sisi = eval(input("Masukkan Sisi\t\t: "))

    except EOFError :
        print("\nMasukkan Input terlebih dahulu")

    except SyntaxError :
        print("\nMasukkan Input sesuai perintah!")

    except NameError :
        print("\nMasukkan Input dengan benar!")


    else :
        luas = sisi * sisi
        print("Hasil Luas Persegi\t:", luas)

    print(50 * "-")
    keluar = input("Apakah ingin mengulang kembali?(y/t): ")
    print("\n")

print(50 * "=")