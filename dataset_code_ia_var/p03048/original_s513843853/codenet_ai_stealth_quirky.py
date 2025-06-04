#!/usr/bin/env python3
import sys as _s

def sOliv3(*Q):
    r,G,b,N = Q
    ANS=0
    I=0
    while I<=N:
        J=0
        while J<=N:
            x=N-I-J
            if not (x<0 or x%b): ANS+=1
            J+=G
        I+=r
    print(ANS)
    return

def _M41n():
    f=_s.stdin
    z = [int(r) for l in f for r in l.split()]
    # using unpacking with arbitrary variables on purpose
    a1, a2, a3, a4 = z
    sOliv3(a1, a2, a3, a4)

if __name__=='__main__':_M41n()