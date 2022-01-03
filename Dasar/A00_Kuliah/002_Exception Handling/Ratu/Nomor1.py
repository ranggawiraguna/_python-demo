for i in range (3) :

    print(30 * "*")
    print("{:^30}".format("Program Hitung"))
    print(30 * "*")

    try:
        A=int(input("Masukkan Nilai A:"))
        B=int(input("Masukkan Nilai B:"))
        C=int(input("Masukkan nilai C:"))
        hasil= (A*B)/C

    except ZeroDivisionError:
          print("\n Nilai C tidak boleh Error")
    except ValueError:
          print("\n Jangan Dimasukkan Huruf")
    except NameError:
          print("\n Variabel tidak ditemukkan")
    except EOFerror:
          print("\n Jangan Keluar Dulu")
    except SyntaxError:
        print("\n Masukkan Input dengan Benar")

    else:
         print("Nilai A:",A)
         print("Nilai B:",B)
         print("Nilai C:",C)
         print("hasil (A*B)/C",hasil)
         print("Variabel ditemukan")