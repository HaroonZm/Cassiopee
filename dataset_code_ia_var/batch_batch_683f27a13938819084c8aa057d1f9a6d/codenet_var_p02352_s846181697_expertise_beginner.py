import sys

# Constantes globales
inf = 10 ** 20

# Fonctions pour lire l'entrée
def LI():
    return list(map(int, sys.stdin.readline().split()))

def JA(a, sep):
    return sep.join(map(str, a))

class RangeAddMin:
    def __init__(self, n):
        i = 1
        while 2 ** i <= n:
            i += 1
        self.N = 2 ** i
        self.A = [0] * (self.N * 2)
        self.B = [0] * (self.N * 2)

    def add(self, a, b, x, k, l, r):
        if b <= l or r <= a:
            return
        if a <= l and r <= b:
            self.A[k] += x
        else:
            m = (l + r) // 2
            self.add(a, b, x, k*2+1, l, m)
            self.add(a, b, x, k*2+2, m, r)
            left = self.B[k*2+1] + self.A[k*2+1]
            right = self.B[k*2+2] + self.A[k*2+2]
            self.B[k] = min(left, right)

    def query(self, a, b, k, l, r):
        if b <= l or r <= a:
            return inf
        if a <= l and r <= b:
            return self.A[k] + self.B[k]
        m = (l + r) // 2
        left = self.query(a, b, k*2+1, l, m)
        right = self.query(a, b, k*2+2, m, r)
        return min(left, right) + self.A[k]

def main():
    n, q = LI()
    qa = []
    for _ in range(q):
        arr = list(map(int, sys.stdin.readline().split()))
        qa.append(arr)
    ram = RangeAddMin(n)
    res = []
    for qi in qa:
        s = qi[1]
        t = qi[2] + 1
        if qi[0] == 0:
            x = qi[3]
            ram.add(s, t, x, 0, 0, n)
        else:
            ans = ram.query(s, t, 0, 0, n)
            res.append(ans)
    return JA(res, "\n")

print(main())