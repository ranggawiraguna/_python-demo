print(50 * "=")
print("{:^50}".format("MENGHITUNG VOLUME KUBUS"))
print((50 * "=") + "\n")

keluar = 'y'
while (keluar == 'y') or (keluar == 'Y'):
    try :
        print(50 * "-")
        sisi = eval(input("Masukkan Sisi\t\t\t\t: "))

        if(sisi<=0) :
            raise ValueError

        assert ((sisi%1)==0)

    except EOFError :
        print("\nMasukkan Input terlebih dahulu")

    except SyntaxError :
        print("\nMasukkan Input sesuai perintah!")

    except NameError :
        print("\nMasukkan Input berupa angka!")

    except ValueError :
        print("\nNilai sisi\ntidak boleh Kurang dari sama dengan nol")

    except AssertionError :
        print("\nNilai sisi\ntidak boleh berupa float(koma)")


    else :
        volume = sisi ** 3
        print("Hasil Volume Kubus\t:", volume)

    print(50 * "-")
    keluar = input("Apakah ingin mengulang kembali?(y/t): ")
    print("\n")

print(50 * "=")
