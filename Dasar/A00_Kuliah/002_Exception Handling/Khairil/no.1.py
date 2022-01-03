print(50 * "=")
print("{:^50}".format("MENGHITUNG KELILING LAYANG-LAYANG"))
print((50 * "=") + "\n")

keluar = 'y'
while (keluar == 'y') or (keluar == 'Y'):
    print(50 * "-")

    try:
        a = eval(input("Masukkan Sisi (a)\t\t: "))
        b = eval(input("Masukkan Sisi (b)\t\t: "))
        c = eval(input("Masukkan Sisi (c)\t\t: "))
        d = eval(input("Masukkan Sisi (d)\t\t: "))
        hasil = (a + b + c + d)

    except EOFError:
        print("\nMasukkan Input terlebih dahulu")
        keluar = 'keluar'

    except SyntaxError:
        print("\nMasukkan Input sesuai perintah!")

    except NameError:
        print("\nMasukkan Input dengan benar!")

    except ValueError:
        print("\nNilai yang dimasukkan\ntidak boleh Kurang dari sama dengan nol")

    except AssertionError:
        print("\nNilai yang dimasukkan\ntidak boleh berupa float(koma)")

    else:
        print("Hasil Keliling\t\t\t:", hasil)

        print(50 * "-")
        keluar = input("Apakah ingin mengulang kembali?(y/t): ")
        print("\n")

print(50 * "=")