from functools import reduce
from itertools import count, cycle, chain, islice

a, b, c = map(int, input().split())
mod = 60
used = set()
# Infinite generator for "now" values
def nowstream(start, a, b):
    return (
        reduce(lambda acc, _: acc[1] + b, 
               range(i), 
               (start, start + a))[1]
        for i in count(0)
    )

def in_window(n, start, end, mod):
    cases = [
        (start % mod < end % mod and start % mod <= n <= end % mod),
        (start % mod >= end % mod and (start % mod <= n < mod or 0 <= n <= end % mod))
    ]
    return any(cases)

for now in nowstream(0, a, b):
    sleep_start = now + a
    if in_window(c, now, sleep_start, mod):
        print((now // mod) * mod + c)
        break
    if now % mod in used:
        print(-1)
        break
    used.add(now % mod)