class BinaryIndexedTree(object):
    def __init__(self, n: int) -> None:
        self.size = n
        self.bit = [0] * (self.size + 1)

    def add(self, i: int, v: int) -> None:
        while (i <= self.size):
            self.bit[i] += v
            i += (i & -i)  # i & -i picks the lowest 1 bit of i.

    def sum(self, i: int) -> int:
        s = 0
        while (i > 0):
            s += self.bit[i]
            i -= (i & -i)
        return s

class RangeQuery(object):
    def __init__(self, n: int) -> None:
        self.size = n
        self.bit1 = BinaryIndexedTree(n + 1)
        self.bit2 = BinaryIndexedTree(n + 1)

    def add(self, i: int, j: int, v: int) -> None:
        self.bit1.add(i, v * -i)
        self.bit1.add(j + 1, v * (j + 1))
        self.bit2.add(i, v)
        self.bit2.add(j + 1, -v)

    def sum(self, i: int, j: int) -> int:
        s = self.bit1.sum(j + 1) + (j + 1) * self.bit2.sum(j + 1)
        s -= self.bit1.sum(i) + i * self.bit2.sum(i)
        return s

if __name__ == "__main__":
    n, q = map(lambda x: int(x), input().split())
    rq = RangeQuery(n)

    for _ in range(q):
        com, *v = map(lambda x: int(x), input().split())
        if (0 == com):
            rq.add(v[0], v[1], v[2])
        else:
            print(rq.sum(v[0], v[1]))