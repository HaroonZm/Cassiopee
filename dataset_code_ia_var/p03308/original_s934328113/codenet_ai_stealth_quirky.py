def rUn(_0, _A):
    __ = sorted(_A)
    return __[-1] - __[0]

readInput = lambda: (int(input()), list(map(int, input().split())))

def EntryPoint():
    q, w = readInput()
    print(rUn(q, w))

if '__main__' == __name__:
    EntryPoint()