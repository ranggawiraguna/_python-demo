from math import pi as phi

def fungsiDecorator(func) :

    def upgradeFunction(*args, **kwargs) :
        print(100*'=')
        print(str(func)[10:-15]+"(", end='')
        print(args[0], end='')

        for item in args[1:(len(args))] :
            print(",",item,end='')

        print(")\n")
        print("[>] fungsiAsli >> return", func(*args, **kwargs))
        print(100*'=')
        print("[>] fungsiUpgrade >> return fungsiAsli >>", end=' ')
        return func(*args, **kwargs)    #Return Fungsi akan sekaligus mengeksekusi statemen didalam fungsi tersebut

    return upgradeFunction

@fungsiDecorator
def printer(text):
    print("[!]", text)

@fungsiDecorator
def luasLingkaran(jari) :
    return phi * (jari**2)

@fungsiDecorator
def luasPersegiPanjang(panjang, lebar) :
    return panjang * lebar

@fungsiDecorator
def volumeBalok(panjang, lebar, tinggi) :
    return panjang * lebar * tinggi


if __name__ == '__main__':

    print(100*'*')
    print("[>]", printer("Rangga Wiraguna"))
    print(100*'*')
    print("\n")

    print(100*'*')
    print(luasLingkaran(5))
    print(100*'*')
    print("\n")

    print(100*'*')
    print(luasPersegiPanjang(10, 5))
    print(100*'*')
    print("\n")

    print(100*'*')
    print(volumeBalok(2, 3, 10))
    print(100*'*')
    print("\n")
