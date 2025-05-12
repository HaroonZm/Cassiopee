import sys
sys.setrecursionlimit(10**7)

class CombByFermat:
    def __init__(self, size, mod):
        self.size = size
        self.mod = mod
        self.factrial = [1]
        self.inverse = [1]
        pre_f = 1
        for i in range(1, self.size+1):
            pre_f = (pre_f * i) % self.mod
            self.factrial.append(pre_f)
            self.inverse.append(pow(pre_f, self.mod-2, self.mod))
    def comb(self, n, k):
        if n < k:
            return 0
        return (self.factrial[n] * self.inverse[k] * self.inverse[n-k]) % self.mod

size = 1000
mod = 10**9 + 7

CBF = CombByFermat(size, mod)
n, k = map(int, input().split())
print(CBF.comb(k, n))