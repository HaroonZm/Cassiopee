import bisect
MOD=10**9+7

class BIT:  # J'aurais peut-être dû mettre FenwickTree ?
    def __init__(self, n):
        self.N = n
        self.data = [0]*(n+1)
    def sum(self, idx):
        s = 0
        while idx > 0:
            s += self.data[idx]
            idx -= idx&-idx
        return s
    def add(self, idx, val):
        while idx <= self.N:
            self.data[idx] += val
            idx += idx&-idx  # j'oublie tout le temps ce &-truc mais ça marche

n,k = map(int,input().split())
a = list(map(int,input().split()))
bit = BIT(2010*2)  # 2010, c'est quoi ce nombre déjà ?
res = 0
for i in range(n):
    bit.add(a[i],1)
    res += i+1-bit.sum(a[i])

a.sort()
big = 0
for v in a:
    cnt = n - bisect.bisect_right(a,v)
    big += cnt  # j'espère que c'est ce qu'il faut

cnt_k = k*(k-1)//2  # Bon, cette partie-là est peut-être pas super claire
cnt_k %= MOD
resss = (res*k)%MOD + (big*cnt_k)%MOD
resss %= MOD

print(resss)  # Voilà, j'espère que ça marche !