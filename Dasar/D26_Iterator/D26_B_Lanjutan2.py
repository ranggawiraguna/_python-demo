class infinite :
    '''Infinite iterator yang mengembalikan bilangan pangkat 2'''

    def __iter__(self):
        self.iterable = 0
        return self

    def __next__(self):
        buffer = 2 ** self.iterable
        self.iterable += 1
        return buffer

if __name__ == '__main__':

    print("BILANGAN PANGKAT\n")

    object_iterator = iter(infinite())

    while True :
        print("{:<7} :".format(('['+str(object_iterator.iterable)+']')),next(object_iterator),end=' ')
        input()