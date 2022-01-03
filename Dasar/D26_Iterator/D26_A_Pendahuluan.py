# Iterator
# Objek yang dapat digunakan sebagai bahan iterasi

#===========================================================================================================================================
#ITERATOR IN ITERABLE
dataList = [20, 6, 2000, 15, 3, 2000]
iterator = iter(dataList)

try :
    print(50*'=')
    print(iterator)
    print()
    print(dataList, end='\n\n')
    print("[1]", next(iterator))
    print("[2]", next(iterator))
    print("[3]", next(iterator))
    print("[4]", next(iterator))
    print("[5]", next(iterator))
    print("[6]", next(iterator))
    print(50*'=')

    print("[7]", next(iterator))

except StopIteration :
    pass
#===========================================================================================================================================

#===========================================================================================================================================
#ITERATOR IN ITERABLE
dataList = [20, 6, 2000, 15, 3, 2000]
iterator = iter(dataList)

try :
    print(50*'=')
    print(iterator)
    print()
    print(dataList, end='\n\n')
    print("[1]", iterator.__next__())
    print("[2]", iterator.__next__())
    print("[3]", iterator.__next__())
    print("[4]", iterator.__next__())
    print("[5]", iterator.__next__())
    print("[6]", iterator.__next__())
    print(50*'=')

    print("[7]", iterator.__next__())

except StopIteration :
    pass
#===========================================================================================================================================

#===========================================================================================================================================
#ITERATOR IN ITERABLE

dataList = [20, 6, 2000, 15, 3, 2000]
iterator = iter(dataList)

print(50*'=')
print(iterator)
print()
print(dataList, end='\n\n')

while True :
    try :
        print("[>]", next(iterator))

    except StopIteration :
        break

print(50*'=')
#===========================================================================================================================================

pause = input("[!]Press ENTER to continue!")

#===========================================================================================================================================
#INFINITE ITERATOR

iterator = iter(int, 1)

print(50*'=')
print(iterator)
print('\n')

while True :
    try :
        print("[>]", next(iterator))

    except StopIteration :
        break
print(50*'=')
#===========================================================================================================================================