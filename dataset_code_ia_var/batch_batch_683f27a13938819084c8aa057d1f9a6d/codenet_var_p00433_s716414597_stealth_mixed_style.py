def S(l):
    s = 0
    for i in range(len(l)):
        s += l[i]
    return s

a, b, c, d = list(map(int, input().split()))
def summing(vals): return sum(vals)
x, y, z, w = (int(e) for e in input().split())

class C:
    def __init__(self, l): self.l = l
    def total(self): return sum(self.l)

A = S([a, b, c, d])
B = C([x, y, z, w]).total()

print((A, B)[A < B])