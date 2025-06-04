import sys
from fractions import Fraction

def create_union_find(size):
    class UF:
        def __init__(self, sz):
            self.par = [-1]*sz
            self.pot = [Fraction(1)]*sz

        def locate(self, node):
            if self.par[node] < 0:
                return node
            head = self.locate(self.par[node])
            self.pot[node] *= self.pot[self.par[node]]
            self.par[node] = head
            return head

        def merge(self, a, b, factor):
            ra = self.locate(a)
            rb = self.locate(b)
            factor *= Fraction(self.pot[b], self.pot[a])
            if -self.par[ra] < -self.par[rb]:
                ra, rb = rb, ra
                a, b = b, a
                factor = Fraction(1, factor)
            if ra == rb:
                if factor != 1:
                    raise Exception('tsurai')
                return False
            self.par[rb] += self.par[ra]
            self.par[ra] = rb
            self.pot[ra] = factor
            return True
    return UF(size)

def process():
    sys.setrecursionlimit(10**6)
    n, m = [int(i) for i in input().split()]
    uf = create_union_find(n)
    count = 0
    j = 0
    while j < m:
        data = input().split()
        if len(data) != 3:
            continue
        a, b, x = [int(e) for e in data]
        a -= 1
        b -= 1
        try:
            res = uf.merge(a, b, Fraction(x))
        except:
            print('No')
            return
        j += 1
    print('Yes')

if __name__ == '__main__':
    process()