from itertools import cycle, islice, chain
class RingList(list):
    def __init__(self, data):
        super().__init__(data)
        self.idx = 0
    def take(self, n):
        segment = [self[(self.idx + i) % len(self)] for i in range(n)]
        self.idx = (self.idx + n) % len(self)
        return segment
while True:
    try:
        line = (lambda s=iter(iter(raw_input, None)): next(s))()
        n, r = map(int, line.split())
        cs_line = raw_input()
        cs = list(map(int, cs_line.split())) if r > 1 else [int(cs_line)]
    except:
        break
    half = n // 2
    A, B = range(half, n), range(half)
    A, B = RingList(list(A)), RingList(list(B))
    for c in cs:
        C = []
        total = n
        while total > 0:
            taken = list(chain(A.take(c), B.take(c)))
            C.extend(taken)
            total -= 2 * c
        A = RingList(C[half:])
        B = RingList(C[:half])
    print(A[-1])