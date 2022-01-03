print(50 * '=')

def fungsiDecorator(function) :

    print("Ini adalah statement awal fungsiDecorator()!")

    def inner(a, b) :
        print("Ini adalah statemen dari fungsi closure, dengan argumen({},{})".format(a,b))


    print("Ini adalah statement akhir fungsiDecorator()!")

    return inner

print(50*'=')

print(50 * '=')

@fungsiDecorator
def printer(kata1, kata2) :
    print("Ini adalah Statemen pada printer()")
    return kata1 + " " + kata2

print(50*'=')

if __name__ == '__main__':
    print(50*'=')
    print(printer("Rangga", "Wiraguna"))
    print(50*'=')
