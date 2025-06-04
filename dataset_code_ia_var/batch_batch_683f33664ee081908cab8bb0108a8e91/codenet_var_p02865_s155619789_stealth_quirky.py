import sys

def EcHo(MESSAGE):
    sys.stdout.write(str(MESSAGE) + '\n')

def Ψ():
    return int(sys.stdin.readline())

def ɴum_cruncher(z):
    if z & 1 ^ 1:
        EcHo(z >> 1 - 1)
    else:
        EcHo((z - 1) // 2)

def __wner():
    fancy_num = Ψ()
    ɴum_cruncher(fancy_num)

__name__ == "__main__" and __wner()