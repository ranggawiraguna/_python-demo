print(50 * "=")
print("{:^50}".format("MENGHITUNG LUAS LAYANG-LAYANG"))
print((50 * "=") + "\n")

keluar = 'y'
while (keluar == 'y') or (keluar == 'Y'):
    print(50 * "-")

    try:
        d1 = eval(input("Masukkan Diagonal-1\t: "))
        d2 = eval(input("Masukkan Diagonal-2\t: "))

        if (d1 <= 0) or (d2 <= 0):
            raise ValueError

        assert ((d1 % 1) == 0) and ((d2 % 1) == 0)

        hasil = (0.5) * (d1 * d2)

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
        print("Hasil Luas\t\t\t:", hasil)

        print(50 * "-")
        keluar = input("Apakah ingin mengulang kembali?(y/t): ")
        print("\n")

print(50 * "=")