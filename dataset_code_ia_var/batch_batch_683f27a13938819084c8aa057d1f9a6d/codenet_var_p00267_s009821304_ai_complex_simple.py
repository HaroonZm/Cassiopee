from functools import reduce
from itertools import chain, repeat, islice, tee, count

def rec_count_sort(mx, arr):
    def upd(f, v): f[v] += 1; return f
    freq = reduce(upd, arr, [0]*(mx+1))
    nmax = max(chain([0], arr))
    def gen():
        for i in range(nmax, -1, -1):
            for _ in repeat(None, freq[i]):
                yield i
    return list(islice(gen(), len(arr)))

def mainloop():
    _ = lambda: int(input())
    __ = lambda: list(map(int, input().split()))
    while True:
        n = _()
        if not n: break
        a, b = rec_count_sort(100000, __( )), rec_count_sort(100000, __( ))
        # two iterators: one for indexation, one for peeking
        idx, _b = tee(count(-1), 2)
        ans = n
        def solve():
            for k in range(0, n, 2):
                i = next(idx)
                if a[k] > b[i+1]:
                    return k+1
            return n
        ans = solve()
        print(["NA", ans][ans != n])
mainloop()