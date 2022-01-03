print(50 * "=")
print("{:^50}".format("MENGHITUNG LUAS ALAS TABUNG"))
print((50 * "=") + "\n")
print(50 * "-")

keluar = 'y'
while (keluar == 'y') or (keluar == 'Y'):
    try :
        jari = eval(input("Masukkan Jari-jari\t\t: "))

    except EOFError :
        print("\nMasukkan Input terlebih dahulu")

    except SyntaxError :
        print("\nMasukkan Input sesuai perintah!")

    except NameError :
        print("\nMasukkan Input dengan benar!")

    else :
        luas = 3.14 * jari * jari
        print("Hasil Luas Alas\t:", luas)

    print(50 * "-")
    keluar = input("Apakah ingin mengulang kembali?(y/t): ")
    print("\n")

print(50 * "=")