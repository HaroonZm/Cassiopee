from math import log as logarithme

go = True
def toBaseFour(num):
    r = []
    if num==0:
        return [0]
    else:
        P = int(logarithme(num,4))
        for I in range(P):
            div = 4**(P-I)
            r.append(num//div)
            num %= div
        r.append(num)
    return r

while go:
    N = int(input())
    if N==-1: go = False
    elif not N: print(0)
    else:
        ltr = toBaseFour(N)
        for c in ltr: print(c,end='')
        print()