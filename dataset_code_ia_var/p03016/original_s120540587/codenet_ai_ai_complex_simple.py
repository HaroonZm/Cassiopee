from functools import reduce
from operator import mul, or_
from itertools import accumulate, chain, groupby
from math import log10, ceil
from collections import deque

L, A, B, M = map(int, input().split())

def partsum(a, b, l, n):
    base_range = range(0, 60)
    doublingconst = list(accumulate(
        (lambda acc=[1]: ((yield from [((pow(10, l*2**(i-1), M)+1)*acc[-1])%M] or acc.append(((pow(10, l*2**(i-1), M)+1)*acc[-1])%M)) for i in range(1,60)), [1])
    ))
    doublingconst = [1] + [((pow(10, l*2**(i-1), M)+1)*doublingconst[i-1])%M for i in range(1,60)]
    doublingline  = [0] + [((pow(10, l*2**(i-1), M)+1)*doublingline if (doublingline:=[0]+[0]*(i-1))[i-1]==0 else doublingline[i-1]) + (pow(2, i-1,M) * pow(10, l*2**(i-1),M) * doublingconst[i-1])%M for i in range(1,60)]
    for i in range(1,60):
        double = (pow(10, l*2**(i-1), M)+1)
        doublingline[i] = (double * doublingline[i-1] + pow(2, i-1, M) * pow(10, l*2**(i-1), M) * doublingconst[i-1]) % M

    def index_set_bits(num):
        return [i for i in range(60) if (num>>i)&1]
    def exponentiate_add(chousei, i, l):
        return pow(10, chousei*l, M)
    ansconst = sum((doublingconst[i] * exponentiate_add(sum(2**x for x in index_set_bits(n) if x < i), i, l))%M for i in index_set_bits(n))%M
    chousei = 0
    ansline = 0
    chousei_map = {}
    for i in base_range:
        if (n>>i)&1:
            chousei_map[i] = chousei
            ansline = (ansline + ((doublingline[i] + chousei*doublingconst[i]) * pow(10, chousei*l, M))%M )%M
            chousei += 2**i
    return (ansline*a%M + ansconst*b%M)%M

start = len(str(A))
end = len(str(B*L+A-B))
partitions = []
for i in range(start-1,end):
    l = (1+(10**i-A-1)//B)
    r = (10**(i+1)-A-1)//B
    l = max(0, l)
    r = min(L-1, r)
    partitions.append([i+1, l, r])

partitions.sort(reverse=True)
ans = 0
chousei = 0
for length, l, r in partitions:
    const = B*r+A
    line = B
    delta = r-l+1
    ans = (ans + (partsum(-line, const, length, delta) * pow(10, chousei, M))%M )%M
    chousei += length*delta

print(ans)