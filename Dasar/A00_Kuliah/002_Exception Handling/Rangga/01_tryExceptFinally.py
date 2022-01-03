
for i in range(6) :

    print(100*"=")
    try :
        data = dict()

        print("[>]INPUT BIODATA MAHASISWA")
        data["nama"] = str(input("   Masukkan Nama\t\t\t\t: "))
        data["nim"] = input("   Masukkan NIM\t\t\t\t\t: ")
        data["ipk"] = float(input("   Masukkan IPK\t\t\t\t\t: "))
        data["tahun"] = eval(input("   Masukkan Tahun Akademik\t\t: "))
        print()
        print("[>]DATA BIODATA MAHASISWA")
        print("   nama\t\t\t\t\t\t\t: {}".format(data["nama"]))
        print("   nim\t\t\t\t\t\t\t: {}".format(data["nim"]))
        print("   ipk\t\t\t\t\t\t\t: {}".format(data["ipk"]))
        print("   tahun\t\t\t\t\t\t: {}".format(data["tahun"]))
        print()
        print("[>]CARI DATA MAHASISWA")
        key = input("   Masukkan Kunci yang dicari\t: ")
        print("   Hasil Pencarian\t\t\t\t: {}".format(data[key]))

    except (EOFError, KeyboardInterrupt) as e:
        print()
        print("[!]Error Massage\t\t\t\t: Masukkan data terlebih dahulu!")
        print("[!]Type Error \t\t\t\t\t: {}".format(str(type(e))[8:(len(str(type(e))) - 2)]))
        print("[!]Detail Error \t\t\t\t: {}".format(e))

    except SyntaxError as e:
        print()
        print("[!]Error Massage\t\t\t\t: Masukkan data sesuai perintah!")
        print("[!]Type Error \t\t\t\t\t: {}".format(str(type(e))[8:(len(str(type(e))) - 2)]))
        print("[!]Detail Error \t\t\t\t: {}".format(e))

    except NameError as e:
        print()
        print("[!]Error Massage\t\t\t\t: Masukkan data sesuai perintah!!")
        print("[!]Type Error \t\t\t\t\t: {}".format(str(type(e))[8:(len(str(type(e))) - 2)]))
        print("[!]Detail Error \t\t\t\t: {}".format(e))

    except ValueError as e :
        print()
        print("[!]Error Massage\t\t\t\t: Masukkan data sesuai perintah!")
        print("[!]Type Error \t\t\t\t\t: {}".format(str(type(e))[8:(len(str(type(e))) - 2)]))
        print("[!]Detail Error \t\t\t\t: {}".format(e))

    except KeyError as e :
        print()
        print("[!]Error Massage\t\t\t\t: Kunci yang dicari tidak ditemukan!")
        print("[!]Type Error \t\t\t\t\t: {}".format(str(type(e))[8:(len(str(type(e))) - 2)]))
        print("[!]Detail Error \t\t\t\t: {}".format(e))

    finally :
        print(100 * "=")


