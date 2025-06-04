import sys
from functools import lru_cache

sys.setrecursionlimit(10**6)

@lru_cache(maxsize=None)
def grun(A, K):
    if A < K:
        return 0
    a, b = divmod(A, K)
    if not b:
        return a
    a += 1
    r = A % a
    next_A = ((a - 1) * K - r) // a * a + r
    return grun(next_A, K)

def solve():
    N = int(sys.stdin.readline())
    X = 0
    for _ in range(N):
        A, K = map(int, sys.stdin.readline().split())
        X ^= grun(A, K)
    print('Takahashi' if X else 'Aoki')

if __name__ == '__main__':
    solve()