import sys
readline = sys.stdin.readline
N = int(readline())
*A, = map(int, readline().split())
C = A[:]
C.sort()

MOD = 4253024257
base = 3
B = [0]*N
v = 1
P = Q = 0
for i in range(N):
    B[i] = v
    P += v * A[i]
    Q += v * C[i]
    v = v * base % MOD
if P == Q:
    print(0)
    exit(0)

for i in range(int(readline())):
    x, y = map(int, readline().split()); x -= 1; y -= 1
    p = A[x]; q = A[y]; r = B[y] - B[x]
    P += r * p - r * q
    if P == Q:
        print(i+1)
        break
    A[x], A[y] = q, p
else:
    print(-1)