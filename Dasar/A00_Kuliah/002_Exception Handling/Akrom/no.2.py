print(50 * "=")
print("{:^50}".format("MENGHITUNG KELILING PERSEGI"))
print((50 * "=") + "\n")
print(50 * "-")

keluar = 'y'
while (keluar == 'y') or (keluar == 'Y'):
    try :
        sisi = eval(input("Masukkan Sisi\t: "))

        if(sisi<=0) :
            raise ValueError

        assert ((sisi%1)==0)

    except EOFError :
        print("\nMasukkan Input terlebih dahulu")

    except SyntaxError :
        print("\nMasukkan Input sesuai perintah!")

    except NameError :
        print("\nMasukkan Input dengan benar!")

    except ValueError :
        print("\nNilai sisi\ntidak boleh Kurang dari sama dengan 0")

    except AssertionError :
        print("\nNilai sisi\ntidak boleh berupa float(koma)")

    else :
        keliling = sisi * 4
        print("Hasil Keliling\t:", keliling)

    print(50 * "-")
    keluar = input("Apakah ingin mengulang kembali?(y/t): ")
    print("\n")

print(50 * "=")