import sys

INF = 2**31 - 1

class RUQ:

    def __init__(self, n):
        tmp = 1
        while tmp < n:
            tmp *= 2
        self.n = tmp * 2
        self.A = [INF] * (2 * self.n - 1)

    def update(self, a, b, x=-1, k=0, l=0, r=0):
        if r <= a or b <= l:
            return
        if a <= l and r <= b:
            if x >= 0:
                self.A[k] = x
            return
        if self.A[k] != INF:
            self.A[k*2+1] = self.A[k*2+2] = self.A[k]
        self.A[k] = INF
        self.update(a, b, x, k*2+1, l, (l+r)/2)
        self.update(a, b, x, k*2+2, (l+r)/2, r)

line = sys.stdin.readline()
n, q = map(int, line.split())
ruq = RUQ(n)
for i in range(q):
    line = sys.stdin.readline()
    if line[0] == "0":
        com, s, t, x = map(int, line.split())
        ruq.update(s, t+1, x, 0, 0, ruq.n)
    else:
        com, i = map(int, line.split())
        ruq.update(i, i+1, -1, 0, 0, ruq.n)
        print(ruq.A[i+ruq.n-1])