print(50 * "=")
print("{:^50}".format("MENGHITUNG KELILING PERSEGI PANJANG"))
print((50 * "=") + "\n")
print(50 * "-")

keluar = 'y'
while (keluar == 'y') or (keluar == 'Y'):
    try :
        panjang = eval(input("Masukkan Panjang\t\t\t\t: "))
        lebar = eval(input("Masukkan Lebar\t\t\t\t\t: "))

        if(panjang<=0) or (lebar<=0) :
            raise ValueError

        assert ((panjang%1)==0) and ((lebar%1)==0)

    except EOFError :
        print("\nMasukkan Input terlebih dahulu")

    except SyntaxError :
        print("\nMasukkan Input sesuai perintah!")

    except NameError :
        print("\nMasukkan Input dengan benar!")

    except ValueError :
        print("\nNilai panjang/lebar\ntidak boleh Kurang dari sama dengan 0")

    except AssertionError :
        print("\nNilai panjang/lebar/tinggi\ntidak boleh berupa float(koma)")

    else :
        keliling = panjang * lebar * 2
        print("Hasil keliling\t:", keliling)

    print(50 * "-")
    keluar = input("Apakah ingin mengulang kembali?(y/t): ")
    print("\n")

print(50 * "=")