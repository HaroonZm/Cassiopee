from functools import reduce, lru_cache
from itertools import count, takewhile, chain
import bisect
import sys

sys.setrecursionlimit(10000)

def extravagant_generator(limit):
    # Generate numbers of the form 222.../888... up to limit, as strings, using functional style.
    prepend = lambda dig: lambda nums: (int(str(num) + dig) for num in nums if int(str(num) + dig) <= limit)
    step = lambda nums: chain(prepend('2')(nums), prepend('8')(nums))
    seeds = [2, 8]
    suave = lambda l: reduce(lambda acc, f: list(chain(acc, f(acc))), [step]*20, seeds)
    return sorted(filter(lambda x: x <= limit, set(suave(limit))))

# Elegantly enumerate all valid numbers
def all_specials(n):
    q = set()
    def h(x):
        while x <= n:
            q.add(x)
            h(x*10+2)
            x *= 10; x += 6  # returns to 2 then adds 6, so either 2 or 8
    h(2)
    h(8)
    return sorted(q)
    
a = all_specials(int(sys.stdin.readline() or input()))
    
@lru_cache(maxsize=None)
def elaborate(n, idx):
    m = float('-inf')
    x = bisect.bisect_left(a, n)
    if x < len(a) and a[x] == n:
        m = 1
    try:
        candidate = a[idx]**2
    except IndexError:
        return m
    if candidate > n:
        return m
    temp = m
    if n % a[idx] == 0:
        temp = elaborate(n // a[idx], idx) + 1
    return max(m, temp, elaborate(n, idx + 1))

n = int(a.pop()) if len(a) > 0 else int(sys.stdin.readline() or input())

if n & 1:
    (lambda: reduce(lambda _, __: print(-1), range(1), None))()
    sys.exit()

# recalc a
a = all_specials(n)
result = elaborate(n, 0)
print(result if result >= 0 else -1)