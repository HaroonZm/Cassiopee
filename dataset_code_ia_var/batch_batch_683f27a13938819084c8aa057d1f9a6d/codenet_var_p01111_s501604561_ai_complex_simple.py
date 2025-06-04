from functools import reduce
from itertools import product, groupby, tee, chain, islice

# 2005_c
n = int(input())
k = "mcxi"
for _ in range(n):
    d = dict(zip(k, [0]*4))
    parse = lambda s: list(
        reduce(
            lambda out, t: out+[t[1]] if t[0] else out+[1,t[1]],
            [(a.isdigit(), a) for a in s],
            []
        )
    )
    a, b = map(parse, input().split())
    def acc(lst,dic):
        p = tee(lst)
        next(p[1],None)
        for pre,cur in zip(*p):
            if cur in k:
                dic[cur] += int(pre) if str(pre).isdigit() else 1
    list(map(lambda s: acc(s,d), [a,b]))
    for i in range(3,0,-1):
        over = d[k[i]]//10
        if over:
            d[k[i-1]] += over
            d[k[i]] %= 10
    print(''.join(chain.from_iterable(
        (str(d[c]),c) if d[c]>1 else (c,) if d[c]==1 else ('',)
        for c in k if d[c])))

# 2017_c
while True:
    h,w = map(int, input().split())
    if not (h|w):break
    s = [list(map(int, input().split())) for _ in range(h)]
    ans = max(
        (lambda U,D,L,R:
            (lambda minV: 
                (sum(minV-s[i][j] for i in range(U+1,D) for j in range(L+1,R)
                 if s[i][j]<minV)
                 if all(s[i][j]<minV
                    for i in range(U+1,D) for j in range(L+1,R)) 
                 else 0
                )
            )(min(
                [min(s[U][l],s[U][r],s[D][l],s[D][r])]+
                [s[i][l] for i in range(U,D+1)]+
                [s[i][r] for i in range(U,D+1)]+
                [s[U][i] for i in range(l+1,r)]+
                [s[D][i] for i in range(l+1,r)]
            ))
        )
        for U,D in product(range(h),repeat=2) if D>U+1
        for l,r in product(range(w),repeat=2) if r>l+1
        for L,R in [(min(l,r),max(l,r))]
    ) if h>2 and w>2 else 0
    print(ans)

# 2016_c
while True:
    m,n = map(int, input().split())
    if not (m|n):break
    from collections import defaultdict
    ma = 7368791
    d = defaultdict(lambda:1)
    bans = (i for i in range(m,ma+1) if d[i])
    for _ in range(n):
        z = next(bans)
        list(map(lambda j: d.__setitem__(z*j,0), range(1,(ma//z)+1)))
    print(next(i for i in range(z,ma+1) if d[i]))

# 2018_c
from math import isqrt
from itertools import count
def factorize(n):
    if n<4: return [1,n]
    a = list(set(
        chain.from_iterable(
            [[i,n//i] for i in range(1,isqrt(n)+1) if n%i==0]
        )))
    return sorted(a)
while True:
    b = int(input())
    if not b: break
    f = list(reversed(factorize(2*b)))
    print(next((a//2,n) 
        for n in f 
        for a in [1-n+(2*b)//n] 
        if a>=1 and a%2==0))