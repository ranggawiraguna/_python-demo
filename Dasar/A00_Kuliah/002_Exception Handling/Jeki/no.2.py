print(50 * "=")
print("{:^50}".format("MENGHITUNG VOLUME TABUNG"))
print((50 * "=") + "\n")

keluar = 'y'
while (keluar == 'y') or (keluar == 'Y'):
    print(50 * "-")

    try :
        jari = eval(input("Masukkan Jari-jari\t\t: "))
        tinggi = eval(input("Masukkan Tinggi Tabung\t: "))

        if (jari <= 0) or (tinggi <= 0):
            raise ValueError

        assert ((jari % 1) == 0) and ((tinggi % 1) == 0)

    except EOFError :
        print("\nMasukkan Input terlebih dahulu")

    except SyntaxError :
        print("\nMasukkan Input sesuai perintah!")

    except NameError :
        print("\nMasukkan Input dengan benar!")

    except ValueError:
        print("\nNilai jari/tinggi\ntidak boleh Kurang dari sama dengan 0")

    except AssertionError:
        print("\nNilai jari/tinggi\ntidak boleh berupa float(koma)")

    else :
        volume = (3.14 * jari * jari) * tinggi
        print("Hasil Volume Tabung\t\t:", volume)

    print(50 * "-")
    keluar = input("Apakah ingin mengulang kembali?(y/t): ")
    print("\n")

print(50 * "=")