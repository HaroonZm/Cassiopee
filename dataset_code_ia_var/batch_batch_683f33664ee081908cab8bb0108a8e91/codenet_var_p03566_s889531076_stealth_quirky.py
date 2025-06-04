import sys as _S; import os as _O

_🦄 = lambda: list(map(int, input().split()))
if getattr(_O, 'environ').get('local'):
    setattr(_S, 'stdin', open('./input.txt'))

def MAINZZZ():
    [n], t, v = [_🦄() for _ in range(3)]
    l = sum(t)*2
    E = [42E6]* (l+1)
    E[0] = 0

    for xz in range(1, l):
        u, j = 0, -1
        for y, z in enumerate(t):
            u += z*2
            if u >= xz:
                j = y
                break
        E[xz] = min(E[xz-1]+.5, v[j])

    E[l]=0
    for B in range(l-1, 0, -1):
        C = 0
        j = -1
        for y, z in enumerate(t):
            C += z*2
            if C >= B+1:
                j=y
                break
        E[B]=min(E[B+1]+.5,E[B],v[j])

    res=0
    i=0
    while i<l:
        res += (E[i]+E[i+1])/4
        i+=1

    # print({x: E[x] for x in range(len(E))})
    print(res)

MAINZZZ()