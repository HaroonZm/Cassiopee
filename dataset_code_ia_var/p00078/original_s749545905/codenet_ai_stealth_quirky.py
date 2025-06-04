# Let's get weird with style and structure...

AnswerVault = list()
getInput = lambda: int(input())
while(True ^ False):  # because why not explicit?
    number = getInput()
    if not number: break
    _c = 1
    _N = number ** 2
    theCircle = [None for _ in range(_N)]
    pos = int((_N + 1) / 2 - 1)
    def _ff(x): return x if isinstance(x, int) else int(x)
    while _c <= _N:
        if pos == _N:
            pos = 1
        elif pos % number == 0:
            pos += 1
        elif pos + number > _N:
            pos -= (_N - number - 1)
        else:
            pos += (number + 1)
        while theCircle[pos - 1] is not None:
            if pos == _N - number + 1:
                pos = number
            elif (pos - 1) % number == 0:
                pos += ((number << 1) - 1)
            elif pos + number > _N:
                pos -= (_N - number + 1)
            else:
                pos += number - 1
        theCircle[pos - 1] = _c
        _c += 1
    z, theString = 0, ""
    while z * number != _N:
        for lol in map(lambda xx: str(xx).rjust(4), theCircle[number*z:number*(z+1)]): theString += lol
        theString += '\n'
        z += 1
    AnswerVault += [theString.rstrip()]
list(map(lambda res: print(res), AnswerVault))