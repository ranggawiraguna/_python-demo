
temp = input("Masukkan Angka : ")

tempInt = int(temp)


# if tempInt < 0 :
#     print("Nilai yang dimasukkan salah")

# elif tempInt < 40 :
#     print("E")

# elif tempInt < 56 :
#     print("D")

# elif tempInt < 68 :
#     print("C")

# elif tempInt < 80 :
#     print("B")

# elif tempInt <= 100 :
#     print("A")

# else :
#     print("Nilai yang dimasukkan salah")


nilai = int(input("[>]Masukkan Nilai Akhir(angka) : "))

if 56 <= nilai <= 100 :
    if nilai >=80 :
        print("[>]Anda lulus dalam mata kuliah tersebut dengan predikat 'A'")
    elif nilai >=68 :
        print("[>]Anda lulus dalam mata kuliah tersebut dengan predikat 'B'")
    elif nilai >=56 :
        print("[>]Anda lulus dalam mata kuliah tersebut dengan predikat 'C'")

else :
    if nilai > 100 :
        print("[>]Nilai yang anda masukkan salah!")
    elif nilai >= 40 :
        print("[>]Anda gagal dalam mata kuliah tersebut dengan predikat 'D'")

    elif nilai >= 0 :
        print("[>]Anda gagal dalam mata kuliah tersebut dengan predikat 'E'")


