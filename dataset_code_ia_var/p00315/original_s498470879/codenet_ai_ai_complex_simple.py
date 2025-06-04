from functools import reduce
from itertools import accumulate, chain, product
from operator import xor
exec('import sys\ninput=sys.stdin.readline\n', globals())
def idx(i, n): return slice(0, n//2) if i == 0 else slice(n//2, n)
(c, n), *lines = (list(map(int, l.split())) for l in sys.stdin)
P = [list(map(int, map(str.__getitem__, l, [0]*n))) for l in lines[:n]]
flip = lambda arr, i, j: arr.__setitem__(i, [arr[i][k] ^ arr[n-1-i][k] if k == j else arr[i][k] for k in range(n)])
rot = lambda arr, i, j: arr.__setitem__(j, [arr[k][j] ^ arr[n-1-k][j] if k == i else arr[k][j] for k in range(n)])
S = [[P[i][j] ^ P[i][n-1-j] for j in range(n//2)] for i in range(n)]
T = [[P[i][j] ^ P[n-1-i][j] for i in range(n//2)] for j in range(n)]
dS = sum(sum(row) for row in S)
dT = sum(sum(col) for col in T)
A = [dS, dT]
ans = int(all(a==0 for a in A))
offset = n//2
ptr = n+1
def trf(z): return (z-1, min(z-1, n-z))
for _ in range(c-1):
    d, *etc = lines[ptr]
    indices = [list(map(int, l)) for l in lines[ptr+1:ptr+1+d]]
    for r, c_ in indices:
        i, j = trf(r), trf(c_)
        S[i[0]][i[1]] ^= 1
        A[0] += 1 - 2*(S[i[0]][i[1]]==0)
        T[j[1]][j[0]] ^= 1
        A[1] += 1 - 2*(T[j[1]][j[0]]==0)
    if not any(A):
        ans += 1
    ptr += d+1
print(ans)