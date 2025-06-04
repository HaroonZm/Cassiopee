class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def bsearch(self, x):
        le = 0
        ri = 1 << (self.size.bit_length() - 1)
        while ri > 0:
            if le + ri <= self.size and self.tree[le + ri] < x:
                x -= self.tree[le + ri]
                le += ri
            ri >>= 1
        return le + 1

n, q = map(int, input().split())
a = list(map(int, input().split()))
bit = BIT(n)
for i, x in enumerate(a):
    bit.add(i, x)
for _ in range(q):
    t, l, r = map(int, input().split())
    if t == 0:
        bit.add(l, r)
    else:
        print(bit.sum(r) - bit.sum(l))