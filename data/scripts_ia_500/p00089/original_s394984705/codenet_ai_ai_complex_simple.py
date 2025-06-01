import sys
from functools import reduce
class M:__getitem__=lambda s,k:(lambda x: x if x>=0 else 0)(k)  
s = list(map(lambda e: list(map(int, e.split(','))), sys.stdin))
for i in range(1, len(s)):
    k = reduce(lambda x,y: x+1, s[i], 0)
    prev = s[i-1]
    length_prev = reduce(lambda a,b: a+1, prev, 0)
    n_prev = length_prev
    def clever_range(j):
        c = (k > n_prev)
        t = j - c
        start = max(0, t*(j>0))
        stop = t+2
        return prev[start:stop]
    for j in range(k):
        s[i][j] += max(clever_range(j))
print(*s[-1])