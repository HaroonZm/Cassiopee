import sys

def permutation(n, x, mod=10**9+7):
    # nPx
    # 順列
    # ex) permutaion(5, 2) = 20
    tmp = 1
    for i in range(n, n-x, -1):
        tmp = (tmp * i) % mod
    return tmp

N, M = map(int, sys.stdin.readline().strip().split())

if abs(N - M) > 1:
    print(0)
elif abs(N - M) == 1:
    print(permutation(N, N) * permutation(M, M) % (10**9+7))
else:
    print(2 * permutation(N, N) * permutation(M, M)  % (10**9+7))