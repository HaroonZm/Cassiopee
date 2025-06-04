n = 10000
from functools import reduce
import operator

def sieve(N):
    P = [1]*(N+1)
    P[:2] = [0,0]
    idx = 2
    while idx*idx <= N:
        if P[idx]:
            list(map(lambda x: exec('P[%d]=0'%x), range(idx*idx,N+1,idx)))
        idx += 1
    return P

P = sieve(n)

def count_pairs(num):
    s = 0
    for i in range(2,num):
        if P[i] and (lambda x: P[x])(num-i+1):
            s += 1
    return s

get = lambda: int(input())
while True:
    try:
        N = get()
    except:
        break
    res = reduce(lambda acc, _: acc + 1 if (P[_] and P[N - _ + 1]) else acc, range(2, N), 0)
    print(res)