class PowTwo :
    '''Kelas yang dapat mengimplementasikan sebuah object_iterator'''

    def __init__(self, maxIter):
        self.maxIter = maxIter

    def __iter__(self):
        self.data = list()
        self.index = 0
        return self

    def __next__(self):
        if self.index <= self.maxIter :
            value = 2 ** self.index
            self.data.append(value)
            self.index += 1

            return value

        else :
            raise StopIteration


if __name__ == '__main__' :
    object_iterator = PowTwo(10)
    object_iterator = iter(object_iterator)
   #object_iterator = iter(PowTwo(10))
    print(150*'=')
    print(object_iterator, end='\n\n')
    while True :
        try :
            print(next(object_iterator), end=' >> ')

        except StopIteration:
            print("STOP[" + str(object_iterator.index) + "]" + "\n")
            print(object_iterator.data)
            break
    print(150*'=')

    object_iterator = iter(PowTwo(10))
    print(150 * '=')
    print(object_iterator, end='\n\n')
    for i in PowTwo(10) :
        print(i, end=' >> ')
        object_iterator.data.append(i)
    else :
        print("STOP[" + str(object_iterator.index) + "]" + "\n")
    print(object_iterator.data)
    print(150 * '=')
