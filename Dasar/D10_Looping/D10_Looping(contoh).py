#Looping

#Looping For

print(50*"=")
print("for in range(awal,--akhir)\n")
for i in range(11,20) :                  #Banyak pengulangan mulai dari 11 s/d --20
    if i is 11:
        print("[>}Bilangan\t: " + str(i))

    else :
        print("\t\t\t  " + str(i))

print(50*"=")
print("for in range(default=0,--akhir)\n")
for i in range(8) :                  #Banyak pengulangan mulai dari default=0 s/d --8
    if i is 0:
        print("[>]Oktal\t: " + str(i))

    else :
        print("\t\t\t  " + str(i))

print(50*"=")
print("for in reversed(range(argumen))\n")
for i in reversed(range(1,11)) :                  #Banyak pengulangan mulai dari 1 s/d --11 yang dibalik
    if i is 10:
        print("[>]Reversed\t: " + str(i))

    else :
        print("\t\t\t  " + str(i))

print(50*"=")
print("for in String\n")
var="RANGGA"
for i in var:                  #Banyak pengulangan mulai dari Karakter awal-akhir
    if i is var[0]:
        print("[>]Huruf\t: " + str(i))

    else :
        print("\t\t\t  " + str(i))

print(50*"=")
print("for in list\n")
var=["Rangga", "1803015106", "Teknik Informatika", "2018"]
for i in var:                  #Banyak pengulangan mulai dari 1 s/d --11 yang dibalik
    if i is var[0]:
        print("[>]Data\t\t: " + str(i))

    else :
        print("\t\t\t  " + str(i))

print(50*"=")
print("for in (data in list)\n")
var=["Rangga", "1803015106", "Teknik Informatika", "2018"]
for i in var:                  #Banyak pengulangan mulai dari 1 s/d --11 yang dibalik
    awal = 0;
    for j in i :
        if awal is 0:
            print("[>]Data\t\t: " + str(j))
            awal += 1

        else :
            print("\t\t\t  " + str(j))
    print()


#Looping while

print(50*"=")
print("While increment\n")

i = 1
while (i<=10) :
    if i is 1:
        print("[>}Bilangan\t: " + str(i))

    else :
        print("\t\t\t  " + str(i))

    i += 1

print(50*"=")
print("While decrement\n")

i = 10
while (i>=1) :
    if i is 10:
        print("[>}Bilangan\t: " + str(i))

    else :
        print("\t\t\t  " + str(i))

    i -= 1

print(50*"=")
print("While input\n")

i = 'Y'
while (i is 'y') or (i is 'Y') :
    print("While akan terus mengulang,\nselama kamu menginput 'y' atau 'Y'")
    i = input("Ingin Mengulang Kembali?(y/t): ")
    print()

print(50*"=")