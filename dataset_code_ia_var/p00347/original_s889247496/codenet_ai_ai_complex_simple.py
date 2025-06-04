import sys
sys.setrecursionlimit(10**7)
from functools import lru_cache
from itertools import accumulate

(w, h), *mat = [[*map(int, l.split())] for l in sys.stdin.read().splitlines()]
S = mat
SW = [list(accumulate(row[::-1]))[::-1] for row in S]
SH = [list(accumulate([S[i][j] for i in range(h)][::-1]))[::-1] for j in range(w)]
SH = [[SH[j][i] for j in range(w)] for i in range(h)]

vec = [(1,0), (0,1)]
def f(op, *args):
    return (max, min)[op%2](*args) if len(args)==2 else (max, min)[op%2](args[0])
@lru_cache(None)
def D(x, y):
    if x>=w or y>=h: return 0
    res = [
        D(x+1,y)-SH[y][x], 
        D(x,y+1)+SW[y][x]
    ]
    return f((x+y)%2, *res)
print(abs(D(0,0)))