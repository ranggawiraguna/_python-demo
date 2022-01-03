print(50 * "=")
print("{:^50}".format("MENGHITUNG VOLUME BALOK"))
print((50 * "=") + "\n")
keluar = 'y'
while (keluar == 'y') or (keluar == 'Y'):
    print(50 * "-")
    try :
        panjang = eval(input("Masukkan Panjang\t\t\t\t: "))
        lebar = eval(input("Masukkan Lebar\t\t\t\t\t: "))
        tinggi = eval(input("Masukkan Tinggi\t\t\t\t\t: "))
        if(panjang<=0) or (lebar<=0) or (tinggi<=0) :
            raise ValueError
        assert ((panjang%1)==0) and ((lebar%1)==0) and ((tinggi%1)==0)

    except EOFError :
        print("\nMasukkan Input terlebih dahulu")
        keluar = ' '
    except SyntaxError :
        print("\nMasukkan Input sesuai perintah!")
    except NameError :
        print("\nMasukkan Input berupa angka!")
    except ValueError :
        print("\nNilai panjang/lebar/tinggi\ntidak boleh Kurang dari sama dengan nol")
    except AssertionError :
        print("\nNilai panjang/lebar/tinggi\ntidak boleh berupa float(koma)")

    else :
        volume = panjang * lebar * tinggi
        print("Hasil Volume Balok\t:", volume)

    print(50 * "-")
    keluar = input("Apakah ingin mengulang kembali?(y/t): ")
    print("\n")

print(50 * "=")
