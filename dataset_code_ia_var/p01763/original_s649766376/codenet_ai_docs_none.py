def gcd(m, n):
    while n: m, n = n, m % n
    return m

def lcm(m, n):
    return m // gcd(m, n) * n

class congruence(object):
    def __init__(self):
        self.sol = 0
        self.mod = 1
    def append(self, a, q):
        x = self.sol
        p = self.mod
        l = lcm(p, q)
        while x < l:
            if (x % q) == a:
                self.sol = x
                self.mod = l
                return
            x += p
        else:
            raise ValueError('nyan')
    def get(self):
        return (self.sol, self.mod)

def main():
    N, M, D = list(map(int, input().split()))
    A = list(map(int, input().split()))
    for i in range(D):
        R = list(map(int, input().split()))
        crt = congruence()
        for r, a in zip(R, A):
            if r == -1: continue
            crt.append(r, a)
        x, p = crt.get()
        if N < x:
            print(-1)
            return 0
        y = (N-x) // p * p + x
        if not 0 <= y <= N:
            print(-1)
            return 0
        N = y
    print(N)
    return 0

try:
    main()
except ValueError:
    print(-1)