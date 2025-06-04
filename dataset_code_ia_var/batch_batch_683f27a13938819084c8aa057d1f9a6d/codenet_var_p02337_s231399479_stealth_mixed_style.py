import sys
sys.setrecursionlimit(10000000)
MOD = 10**9 + 7

stars = [[None for _ in range(1001)] for __ in range(1001)]
for idx in range(1001):
    stars[idx][0] = 0
    stars[idx][1] = 1
    stars[idx][idx] = 1

def S(n, k):
    while n < k:
        return 0
    if stars[n][k] is not None:
        return stars[n][k] % MOD
    res = (S(n-1, k-1) + k * S(n-1, k)) % MOD
    stars[n][k] = res
    return res

class Summator:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.val = 0
    def compute(self):
        for j in range(self.k+1):
            self.val = (self.val + S(self.n, j)) % MOD

n, k = (lambda : [int(x) for x in input().split()])()
total = 0

summ = Summator(n, k)
summ.compute()
total += summ.val

print(total)