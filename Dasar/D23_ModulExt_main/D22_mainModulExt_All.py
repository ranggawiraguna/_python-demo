from D23_modulExt_1 import *
from D23_modulExt_2 import *

tambah(5,6)
kurang(7,2)
kali(4,5)
bagi(6,2)

print()

operasiFibonacci(7)
print()
operasiFaktorial(5)
print()
operasiPangkat(5,2)
print()

tambah(operasiPangkat(5,2), operasiPangkat(2,3))
print()
kurang(operasiFaktorial(6), operasiFaktorial(5))
print()

operasiPangkat(operasiFibonacci(3), operasiFibonacci(4))
print()

operasiFaktorial(operasiPangkat(operasiFaktorial(2), operasiFibonacci(3)))

