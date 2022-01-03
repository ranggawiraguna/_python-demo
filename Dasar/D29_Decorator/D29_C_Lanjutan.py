def listHastag(func):

    def upgradeFunction(*args, **kwargs):
        print(100 * '#')
        func(*args, **kwargs)
        print(100 * '#')


    return upgradeFunction


def listStar(func) :
    def upgradeFunction(*args, **kwargs):
        print(100 * '*')
        func(*args, **kwargs)
        print(100 * '*')

    return upgradeFunction

@listHastag
@listStar
def printer(text) :
    print(text)


if __name__ == '__main__':
    printer("Rangga Wiraguna")