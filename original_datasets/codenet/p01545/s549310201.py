class RangeMaximumQuery:
    def __init__(self, n):
        self.size = n
        self.dat = [0] * (2 * n - 1)
    
    def update(self, i, x):
        i += self.size - 1
        self.dat[i] = x
        while i > 0:
            i = (i - 1) // 2
            d1 = self.dat[i * 2 + 1]
            d2 = self.dat[i * 2 + 2]
            if d1 > d2:
                self.dat[i] = d1
            else:
                self.dat[i] = d2
    
    def getmax(self, a, b, k, l, r):
        if r <= a or b <= l:
            return 0
        elif a <= l and r <= b:
            return self.dat[k]
        else:
            vl = self.getmax(a, b, k * 2 + 1, l, (l + r) // 2)
            vr = self.getmax(a, b, k * 2 + 2, (l + r) // 2, r)
            if vl > vr:
                return vl
            else:
                return vr

def solve():
    from math import ceil, log
    
    n = int(input())
    A = map(int, input().split())
    s = 2 ** ceil(log(n, 2))
    W = RangeMaximumQuery(s)
    for a_i in A:
        cost = W.getmax(0, a_i - 1, 0, 0, s) + a_i
        W.update(a_i - 1, cost)
    ans = n * (n + 1) // 2 - W.getmax(0, n, 0, 0, s)
    print(ans)

solve()