from functools import reduce
from operator import add, itemgetter, ge
from itertools import count

while True:
    N, Q = map(int, input().split())
    if not any((N, Q)):
        break
    D = [0]*100
    list(map(lambda _:list(map(lambda x:D.__setitem__(int(x)-1, D[int(x)-1]+1), input().split()[1:])), range(N)))
    idx, val = max(filter(lambda t: ge(t[1], Q), enumerate(D)), default=(-1,0), key=itemgetter(1))
    print((idx+1) if idx != -1 else 0)