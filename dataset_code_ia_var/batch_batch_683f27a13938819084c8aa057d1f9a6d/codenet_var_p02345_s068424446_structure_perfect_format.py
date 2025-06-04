INITIAL = 2 ** 31 - 1

class SegTreeMin:
    def __init__(self, V):
        self.sz = len(V)
        N = 1
        while N < self.sz:
            N *= 2
        self.N = N
        self.node = [INITIAL] * (2 * self.N - 1)
        for i in range(self.sz):
            self.node[i + self.N - 1] = V[i]
        for i in range(self.N - 2, -1, -1):
            self.node[i] = min(self.node[2 * i + 1], self.node[2 * i + 2])

    def update(self, x, val):
        x += (self.N - 1)
        self.node[x] = val
        while x > 0:
            x = (x - 1) // 2
            self.node[x] = min(self.node[2 * x + 1], self.node[2 * x + 2])

    def get_min(self, a, b, k=0, l=0, r=-1):
        if r < 0:
            r = self.N
        if r <= a or l >= b:
            return INITIAL
        if l >= a and r <= b:
            return self.node[k]
        vl = self.get_min(a, b, 2 * k + 1, l, (l + r) // 2)
        vr = self.get_min(a, b, 2 * k + 2, (l + r) // 2, r)
        return min(vl, vr)

def main():
    n, q = map(int, input().split())
    V = [INITIAL] * n
    seg = SegTreeMin(V)
    for _ in range(q):
        com, x, y = map(int, input().split())
        if com:
            y += 1
            print(seg.get_min(x, y))
        else:
            seg.update(x, y)

if __name__ == "__main__":
    main()