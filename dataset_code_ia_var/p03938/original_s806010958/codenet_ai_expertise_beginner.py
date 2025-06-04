import sys

sys.setrecursionlimit(10**9)
INF = 10**18
MOD = 10**9 + 7

def read_int():
    return int(sys.stdin.readline().strip())

def read_list():
    return list(map(int, sys.stdin.readline().strip().split()))

N = read_int()
P = read_list()
for i in range(len(P)):
    P[i] -= 1

A = [0] * N
B = [0] * N
gap = 30000
for i in range(N):
    A[i] = gap * i + 1
    B[i] = gap * (N - i)

for i in range(N):
    p = P[i]
    A[p] += i

print(' '.join(map(str, A)))
print(' '.join(map(str, B)))