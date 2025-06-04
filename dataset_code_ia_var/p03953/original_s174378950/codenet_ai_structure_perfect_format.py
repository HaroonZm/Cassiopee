import sys
import numpy as np

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
X = [int(x) for x in input().split()]
M, K = map(int, input().split())
A = [int(x) for x in input().split()]

P = list(range(N))
for a in A:
    P[a - 1], P[a] = P[a], P[a - 1]

P = np.array(P, dtype=np.int32)

def power(P, n):
    if n == 1:
        return P
    Q = power(P, n // 2)
    Q = Q[Q]
    return P[Q] if n & 1 else Q

Q = power(P, K)

diff = np.diff([0] + X)
answer = diff[Q].cumsum()
print('\n'.join(answer.astype(str)))