#Mengimport modul pada package sekaligus
from D23_A_perhitungan import Aritmatika
from D23_A_perhitungan import operasiIterasi

Aritmatika.tambah(5, 5)
Aritmatika.kurang(3, 6)
Aritmatika.bagi(3, 6)
Aritmatika.kali(4, 7)
Aritmatika.modulus(5, 8)

print()

operasiIterasi.operasiPangkat(5, 3)
operasiIterasi.operasiFaktorial(5)
operasiIterasi.operasiFibonacci(8)

#Catatan

#{>]from D23_A_perhitungan import Aritmatika,operasiIterasi
#   mengimport modul yang ada pada package secara bersamaan

#{>]from D23_A_perhitungan import Aritmatika as hitung
#   mengimport modul Aritmatika yang ada pada package dengan mengaliaskan nya menjadi hitung

#{>]from D23_A_perhitungan import operasiIterasi as hitung
#   mengimport modul Operasi yang ada pada package dengan mengaliaskan nya menjadi hitung