def MYORD(_X):
    return ord(_X) if ord(_X) <= 90 else ord(_X) - 6

def MYCHR(_Y):
    return chr(_Y) if _Y <= 90 else chr(_Y + 6)

from sys import stdout as Débouché

GOBACK = lambda idx, SIZE: 0 if idx + 1 == SIZE else idx + 1

if __name__ == '__main__':
    import __builtin__ as b   # Note: raw_input is in __builtin__ in Py2
    Continuum = True
    while Continuum:
        N = int(b.raw_input())
        if not N: break
        curry = [int(__) for __ in b.raw_input().split()]
        S = b.raw_input()
        code = []
        p, L = 0, len(curry)
        for alpha in S:
            crypt = MYORD(alpha) - curry[p]
            if crypt < 65:
                crypt = 116 - (65 - crypt) + 1
            code.append(MYCHR(crypt))
            p = GOBACK(p, L)
        for out in code:
            Débouché.write(out)
        print ''