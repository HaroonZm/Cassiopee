from collections import defaultdict
import sys

readline = sys.stdin.readline
write = sys.stdout.write
H, W, N = map(int, readline().split())
A = [0]*W
B = [0]*W
C = [0]*W
for i in range(W//2):
    A[i] = i * 2 + 1
    A[-i-1] = i * 2
    B[i*2] = C[i*2 - 1] = i
    B[-1-i*2] = C[-1-i*2 + 1] = i + W//2
X = list(range(W))
P = [list(map(int, readline().split())) for i in range(N)]
P.sort()
for a, b in P:
    if a % 2 == 1:
        k = a // 2
        m = b//2*2
        p = A[(B[m] + k) % W]
        q = A[(B[m+1] + k) % W]
    else:
        k = a // 2 - 1
        m = (b-1)//2*2
        p = A[(C[m+1] + k) % W]
        q = A[(C[m+2] + k) % W]
    X[p], X[q] = X[q], X[p]

E0 = list(range(W))
for i in range(W//2):
    E0[2*i], E0[2*i+1] = E0[2*i+1], E0[2*i]
E1 = E0[:]
for i in range(W//2-1):
    E1[2*i+1], E1[2*i+2] = E1[2*i+2], E1[2*i+1]
k = H//2
Y = list(range(W))
while k:
    if k & 1:
        Y = [Y[e] for e in E1]
    E1 = [E1[e] for e in E1]
    k >>= 1
if H % 2:
    Y = [Y[e] for e in E0]
ans = [0]*W
for i, e in enumerate(Y):
    ans[X[e]] = i+1
for e in ans:
    write("%d\n" % e)