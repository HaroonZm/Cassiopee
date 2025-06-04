def solve():
    import sys, itertools, functools, operator
    input_stream = sys.stdin

    N, M, Q = map(int, input_stream.readline().split())

    class RotDeque:
        def __init__(self, iterable):
            self.data = list(iterable)
        def rot(self, n):
            n = n % len(self.data) if self.data else 0
            self.data = self.data[-n:] + self.data[:-n]
        def pluck(self):
            res, self.data = self.data[0], self.data[1:]
            return res

    sd = RotDeque(range(N))
    ex = list(itertools.repeat(1, N))

    def rotfun(a):
        sd.rot(a if a % 2 else -a)
        idx = sd.pluck()
        ex[idx] = 0

    list(map(rotfun, map(int, input_stream.readline().split())))

    ql = list(map(int, input_stream.readline().split()))
    print('\n'.join(map(str, map(ex.__getitem__, ql))))

solve()