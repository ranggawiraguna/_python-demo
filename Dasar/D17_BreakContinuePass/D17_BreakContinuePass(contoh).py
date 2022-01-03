# break / continue / pass
# berpengaruh pada satu instruksi looping

print(51*"=")
print("{:^51}".format("DERET BILANGAN GANJIL-GENAP(0-99)"))
print(51*"=")

print(51*"-")
pilihan = int(input("Pilihan\t: [1]GANJIL\n\t\t  [2]GENAP\nPilih\t:  "))
print(51*"-")

print(51 * "-")
judul = str()
key = int()

if pilihan is 1 :
    judul = "{:^51}\n{:^51}\n{:^51}".format((31*"-"), "| DERET BILANGAN GANJIL(0-99) |", (31*"-"))
    key = 1

elif pilihan is 2 :
    judul = "{:^51}\n{:^51}\n{:^51}".format((30*"-"), "| DERET BILANGAN GANAP(0-99) |", (30*"-"))
    key = 0

else :
    print("Note\t: Pilihan yang dimasukkan salah!\n" + (51 * "-"))
    print(51 * "=")
    exit()

print("{:^51}".format(judul))
i = 0
print("|", end=' ')

while True :
    if i > 9:
        break

    for j in range(10) :
        if ((j%2)==key) and (i==0) :
            print("{:>2}".format(j),end=' | ')
        elif ((j%2)==key) and (i!=0) :
            print("{:<2}".format(str(i)+str(j)),end=' | ')
        else :
            continue

    if ((i%2) == 1) :
            print()
            print("|", end=' ')

    else :
        pass

    i += 1

print("\b\b"+(51*"-"))
print(51*"=")