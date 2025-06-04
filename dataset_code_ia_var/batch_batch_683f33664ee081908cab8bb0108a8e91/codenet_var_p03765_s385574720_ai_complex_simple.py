from functools import reduce
from itertools import accumulate, islice, tee
from operator import add

def inp(): return input()
def mapp(f, it): return map(f, it)
def lmap(f, it): return list(mapp(f, it))
def linput(): return lmap(str, inp())
def imap(): return lmap(int, inp().split())

S, T, Q = (inp() for _ in range(3))
Q = int(Q)
I = [lmap(int, inp().split()) for _ in range(Q)]
M, MAP = 3, {"A":1, "B":2}

def RUISEKI(s):
    zero = [0]
    seq = mapp(lambda c: MAP[c], s)
    acc = accumulate(seq, lambda x, y: (x + y) % M, initial=0)
    return list(acc)

SR, TR = RUISEKI(S), RUISEKI(T)

for i in range(Q):
    a,b,c,d = I[i]
    ans1 = ((SR[a-1]<<1) + SR[b])%M
    ans2 = ((TR[c-1]<<1) + TR[d])%M
    print(('NO','YES')[ans1==ans2])