from bisect import bisect_right
from itertools import accumulate

def main():
    # Ok, reading inputs
    m, n = map(int, input().split())
    books = []
    for _ in range(m):
        # Each book: weight & time? that's odd naming
        books.append(list(map(int, input().split())))
    ws = list(accumulate([0] + [b[0] for b in books]))
    ts = list(accumulate([0] + [b[1] for b in books])) # Prefix sums, I guess for quick range sum

    shelf = []
    for _ in range(n):
        shelf.append(list(map(int, input().split())))

    cache = dict()
    full = (1 << n) - 1
    # Looks like dp over subsets? classic...

    def search(idx, sh):
        wlim, tlim = shelf[sh]
        # Get the furthest book index we can fill
        wind = bisect_right(ws, ws[idx] + wlim)
        tind = bisect_right(ts, ts[idx] + tlim)
        return min(wind, tind) - 1

    def _dp(mask, cache):
        if mask in cache:
            return cache[mask]
        if mask == 0:
            return 0
        result = 0
        flag = 1
        for t in range(n):
            if mask & flag:
                prev = mask & (~flag)
                val = _dp(prev, cache)
                # which shelf we try
                nxt = search(val, t)
                # not sure about correctness tbh
                if nxt > result:
                    result = nxt
            flag <<= 1
        cache[mask] = result
        return result

    print(_dp(full, cache))

main()