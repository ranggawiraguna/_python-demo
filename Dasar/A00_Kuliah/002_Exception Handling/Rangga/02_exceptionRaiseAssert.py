
for i in range(4) :

    print(70 * "=")
    print("{:^70}".format("MEMERIKSA NILAI MIN & MAX DARI DATA BILANGAN BULAT"))
    print(70 * "=")

    data = list()

    try :
        n = int(input("[>]Masukkan Banyak Data(Max=10)\t: "))
        print()
        if n > 10 :
            raise IndexError(n)

        for i in range(1,n+1):
            data.append(eval(input("[>]Masukkan Angka-{:<2}\t\t\t: ".format(i))))

        for i in range(len(data)) :
            assert ((data[i]%1) == 0), data[i]

    except (EOFError,SyntaxError,NameError):
        print()
        print("[!]Error, kesalahan input data!")
        print(70 * "=")
        exit()

    except IndexError as e :
        print()
        print("[!]Banyak data = {} melebihi ketentuan kapasitas!".format(e))

    except AssertionError as e :
        print()
        print("[!]Data = {} bukan merupakan bilangan bulat!".format(e))

    else :
        print("[>]Nilai Minimum data\t\t\t:", (min(data)))
        print("[>]Nilai Maksimum data\t\t\t:", (max(data)))

    print(70 * "=")

