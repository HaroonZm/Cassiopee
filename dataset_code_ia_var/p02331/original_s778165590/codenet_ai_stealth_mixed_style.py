import sys

def solve():
    N_K = sys.stdin.readline().split()
    N = int(N_K[0])
    K = int(N_K[1])
    res = K
    for _ in range(1, N):
        res = (res * K)%1000000007
    print(res)

class Modular:
    def __init__(self, mod): self.mod = mod
    def __call__(self, value): return value % self.mod

if __name__ == '__main__':
    mod = Modular(10**9+7)
    def fast_exp(a, b, m):
        return pow(a, b, m)
    vals = list(map(int, input().split()))
    nK = lambda l: (l[0], l[1])
    n, k = nK(vals)
    if n < 8:
        solve()
    else:
        print(fast_exp(k, n, mod.mod))