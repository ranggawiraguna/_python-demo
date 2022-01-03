# import decimal >> decimal.Desimal('angka')
from decimal import Decimal as dec # Menggunakan decimal.Decimal sebagai dec

# import franctions >> fraction.Fraction(angka)
from fractions import Fraction as fract # Menggunakan franctions.Franction sebagai fract

# import franctions >> fraction.Fraction(angka)
import math # Menggunakan modul math.function

#Floating operation
#Pengoperasian float akan menghasilkan nilai yang tidak pasti karena angka float pada python
#disimpan dalam bentuk biner yang tentunya untuk bilangan float akan memiliki panjang biner yang sangat panjang
#sehingga komputer harus mengoperasikannya dengan panjang iner yang terbatas
print(50*"=")
print("MANUAL OPERATION FLOATING NUMBER")
a = 1.1
b = 2.2
print("[>]1.1 + 2.2 =", 1.1 + 2.2) #Perhitungan Manual
print("[>] a  +  b  =", a+b)       #Perhitungan Manual
print("[>]1.1 * 2.2 =", 1.1 * 2.2) #Perhitungan Manual
print("[>] a  +  b  =", a*b)       #Perhitungan Manual

#Modul decimal
#Dengan menggunakan modul decimal pada fungsi decimal kita dapat melakukan operasi float dengan
#hasil pengoperasian yang pasti karena fungsi dec akan menghasilkan suatu string yang diubah
#menjadi bilangan float tetap
print(50*"=")
print("desimal.Decimal('angkaFloat') OPERATION")
a = dec('1.1')                                      #Menggunakan modul decimal
b = dec('2.2')                                      #Menggunakan modul decimal
print("[>]1.1 + 2.2 =", dec('1.1') + dec('2.2'))    #Menggunakan modul decimal
print("[>] a  +  b  =", a+b)                        #Menggunakan modul decimal
print("[>]1.1 * 2.2 =", dec('1.1') * dec('2.2'))    #Menggunakan modul decimal
print("[>] a  *  b  =", a*b)                        #Menggunakan modul decimal

#Modul franctions
#Modul fractions berfungsi untuk menghasilkan bilangan pecahan dari suatu angka
#hasil pecahan dari fungsi fraction akan menghasilkan bilangan float tetap
print(50*"=")
a = dec('1.1')                                             #Menggunakan modul decimal
b = dec('2.2')                                             #Menggunakan modul decimal
print("fraction.Fraction('angka') OPERATION")
print("[>]1.1 + 2.2 =", fract(dec('1.1') + dec('2.2')))           #Menggunakan modul fract
print("[>]1.1 * 2.2 =", fract(dec('1.1')) * fract(dec('2.2')))    #Menggunakan modul fract
print("[>] a  +  b  =", fract(a+b))                               #Menggunakan modul fract
print("[>] a  *  b  =", fract(a) * fract(b))                               #Menggunakan modul fract
print()
a = dec('0.5')                                                    #Menggunakan modul decimal
b = dec('0.4')                                                    #Menggunakan modul decimal
print("[>]1/2 + 2/5 =", fract(1,2) + fract(2,5))                  #Menggunakan modul fract
print("[>] a  *  b  =", fract(a*b))                               #Menggunakan modul fract

#Modul math
#Modul yang berisi banyak fungsi matematika didalamnya, bisa kita gunakan dengan memangil math.function()
print(50*"=")
print("math.function(argumen) OPERATION")
print("[>]Nilai phi  =", math.pi)               #Mengembalikan nilai phi lingkaran
print("[>]cos phi    =", math.cos(math.pi))     #Mengembalikan nilai cosinus x
print("[>]sin(30)    =", math.sin(30))          #Mengembalikan nilai sinus x
print("[>]tan(30)    =", math.tan(30))          #Mengembalikan nilai tangen x
print("[>]exp(10)    =", math.exp(10))          #Mengembalikan nilai eksponensial x
print("[>]log10(100) =", math.log10(100))       #Mengembalikan nilai logaritma x
print("[>]fact(5)    =", math.factorial(5))     #Mengembalikan nilai factorial x
print(50*"=")