import sys
from operator import itemgetter, methodcaller

class BIT:
    __slots__ = ('bit', 'size')
    def __init__(self, size):
        self.size = size
        self.bit = [0] * (size + 2)

    def sum(self, i):
        res = 0
        i += 1
        while i:
            res += self.bit[i]
            i -= i & -i
        return res

    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.bit[i] += x
            i += i & -i

def main():
    readline = sys.stdin.readline
    n, m = map(int, readline().split())
    a = list(map(lambda x: int(x)-1, readline().split()))

    bit0, bit1 = BIT(m+1), BIT(m+1)
    for x, y in zip(a, a[1:]):
        d = (y - x) % m
        bit1.add(0, d)
        if d < 2:
            continue
        nx = (x + 2) % m

        if nx <= y:
            bit0.add(nx, -1)
            bit1.add(nx, nx-1)
            bit0.add(y+1, 1)
            bit1.add(y+1, -(nx-1))
        else:
            bit0.add(nx, -1)
            bit1.add(nx, nx-1)
            b = (0 - (nx-1)) % m
            bit0.add(0, -1)
            bit1.add(0, -b)
            bit0.add(y+1, 1)
            bit1.add(y+1, b)

    ans = min(bit0.sum(i) * i + bit1.sum(i) for i in range(m))
    print(ans)

if __name__ == '__main__':
    main()