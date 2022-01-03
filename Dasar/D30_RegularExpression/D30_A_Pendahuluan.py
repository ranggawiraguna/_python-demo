# Regular Expresion
# Metode pencarian sebuah deret karakter dari sebuah teks dengan pola tertentu

import re #Modul RegularExpression (REGEX)

#Regex Normal
def searchNumberPhone_A(text) :
    nomorTeleponRegex = re.compile(r'\d\d\d\d \d\d\d\d\d\d\d\d')

    matchingObject = nomorTeleponRegex.search(text)

    if (type(matchingObject) is not type(None)):
        print( "[>]Nomor Telepon\t: {}".format(matchingObject.group()) )

    else :
        print("[>]Keterangan\t\t: Nomor Telepon tidak ditemukan")

#Regex Pengelompokkan dengan tandaOperasi ( dan )
def searchNumberPhone_B(text) :
    nomorTeleponRegex = re.compile(r'(\d\d\d\d) (\d\d\d\d\d\d\d\d)')

    matchingObject = nomorTeleponRegex.search(text)

    if (type(matchingObject) is not type(None)):
        print( "[>]Nomor Telepon\t: {0} >> ({1})-({2}) >> {3}".format
               (matchingObject.group(), matchingObject.group(1), matchingObject.group(2), matchingObject.groups()) )

    else:
        print("[>]Keterangan\t\t: Nomor Telepon tidak ditemukan")

#Regex dengan menggunakan karakter escape '\(' dan '\)' >> '(08xx xxxxxxxx)'
def searchNumberPhone_C(text) :
    print() #===============================================================================================================================
    nomorTeleponRegex = re.compile(r'\(\d\d\d\d \d\d\d\d\d\d\d\d\)')

    matchingObject = nomorTeleponRegex.search(text)

    print("nomorTeleponRegex = re.compile(r'\(\d\d\d\d \d\d\d\d\d\d\d\d\)')")
    if (type(matchingObject) is not type(None)):
        print( "[>]Nomor Telepon\t: {}".format(matchingObject.group()) )

    else :
        print("[>]Keterangan\t\t: Nomor Telepon tidak ditemukan")

    print() #===============================================================================================================================
    nomorTeleponRegex = re.compile(r'\(\d\d\d\d\) \d\d\d\d\d\d\d\d')

    matchingObject = nomorTeleponRegex.search(text)

    print("nomorTeleponRegex = re.compile(r'\(\d\d\d\d\) \d\d\d\d\d\d\d\d')")
    if (type(matchingObject) is not type(None)):
        print( "[>]Nomor Telepon\t: {}".format(matchingObject.group()) )

    else :
        print("[>]Keterangan\t\t: Nomor Telepon tidak ditemukan")

    print() #===============================================================================================================================
    nomorTeleponRegex = re.compile(r'(\(\d\d\d\d\)) (\d\d\d\d\d\d\d\d)')

    matchingObject = nomorTeleponRegex.search(text)

    print("nomorTeleponRegex = re.compile(r'(\(\d\d\d\d\)) (\d\d\d\d\d\d\d\d)')")
    if (type(matchingObject) is not type(None)):
        print( "[>]Nomor Telepon\t: {0} >> ({1})-({2}) >> {3}".format
               (matchingObject.group(), matchingObject.group(1), matchingObject.group(2), matchingObject.groups()) )

    else:
        print("[>]Keterangan\t\t: Nomor Telepon tidak ditemukan")



if __name__ == '__main__':

    print(100*'=')
    searchNumberPhone_A(input("[!]Masukkan Pesan\t: "))
    print((100*'=')+'\n')


    print(100*'=')
    searchNumberPhone_B(input("[!]Masukkan Pesan\t: "))
    print((100*'=')+'\n')

    print(100*'=')
    searchNumberPhone_C(input("[!]Masukkan Pesan\t: "))
    print((100*'=')+'\n')




