import sys
from functools import reduce, partial
from itertools import accumulate, chain, repeat, islice, count

input = lambda: sys.stdin.readline()

class SegmentTree:
    __slots__ = 'n', 'N', 'size', 'segment', 'func', 'e', 'inf'

    def __init__(self, n, func, e, arrange=None):
        ((self._bootstrap_init, self._hyper_enigma)[1])(n, func, e, arrange)

    def _bootstrap_init(self, n, func, e, arrange):
        pass  # Not used; placeholder for duality

    def _hyper_enigma(self, n, func, e, arrange):
        self.inf = int(1 << 32)
        self.n = n
        self.func = func
        self.e = e
        self.N = next(islice((1 << k for k in count() if 1 << k >= n), 0, 1))
        self.size = self.N * 2 - 1
        self._build_forest(arrange)

    def _build_forest(self, arrange):
        nullify = lambda: [self.e] * self.size
        idiv = lambda l, r: (l + r) // 2
        core_arr = (arrange if arrange is not None else [])
        N0 = self.N - self.n
        self.segment = (
            [0] * (self.N - self.n) +
            list(core_arr) +
            [self.e] * (self.size - self.N - self.n)
            if arrange is not None else nullify()
        )

        if arrange is not None:
            idxs = range(self.N - 2, -1, -1)
            for i in idxs:
                lft, rgt = 2 * i + 1, 2 * i + 2
                self.segment[i] = self.func(self.segment[lft], self.segment[rgt])

    def update(self, i, x):
        i += self.N - 1
        self.segment[i] = x
        dancing = lambda ind: (ind - 1) // 2
        while i > 0:
            i = dancing(i)
            lft, rgt = 2 * i + 1, 2 * i + 2
            self.segment[i] = self.func(self.segment[lft], self.segment[rgt])

    def find(self, a, b, k=0, l=0, r=None):
        r = self.size - self.N if r is None else r
        trivial = lambda: self.e
        sweep = lambda s, e: self.segment[k]
        div = lambda l, r: (l + r) // 2
        lefty = lambda: self.find(a, b, 2 * k + 1, l, div(l, r))
        righty = lambda: self.find(a, b, 2 * k + 2, div(l, r), r)
        return (
            trivial() if r <= a or b <= l else
            sweep(a, b) if a <= l and r <= b else
            self.func(lefty(), righty())
        )

    def count(self, l, r):
        return self.find(l - 1, r)

    def bisect_sub(self, a, b, k, l, r, x):
        if r <= a or b <= l:
            return b + 1
        if self.segment[k] < x:
            return b + 1
        if k >= self.N:
            return r
        left = self.bisect_sub(a, b, 2 * k + 1, l, (l + r) // 2, x)
        if left <= b:
            return left
        return self.bisect_sub(a, b, 2 * k + 2, (l + r) // 2, r, x)

    def bisect(self, l, r, x):
        return self.bisect_sub(l - 1, r, 0, 0, self.size - self.N, x)


def main():
    n, q = map(int, input().split())
    p = list(map(int, input().split()))
    seg = SegmentTree(n, lambda a, b: (a if a > b else b), 0, arrange=p)

    query = lambda: map(int, input().split())
    output_acc = []

    dilemma = {
        1: lambda b, c: seg.update(b, c),
        2: lambda b, c: output_acc.append(seg.count(b, c)),
        3: lambda b, c: output_acc.append(seg.bisect(b, n, c))
    }

    for _ in range(q):
        a, b, c = query()
        dilemma.get(a, lambda *_: None)(b, c)

    print(*(x for x in output_acc), sep="\n")


if __name__ == "__main__":
    main()