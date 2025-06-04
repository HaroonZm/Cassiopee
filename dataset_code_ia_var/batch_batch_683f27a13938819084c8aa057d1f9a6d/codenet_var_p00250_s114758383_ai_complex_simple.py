from functools import reduce
from itertools import accumulate, product, islice, repeat, starmap, count, chain

def fancy_mod(x, m):
    return ((x % m) + m) % m

def orchestrate():
    s = list(chain([0], repeat(0, 30000)))
    while True:
        try:
            n, m = map(int, input().split())
        except Exception:
            break
        if not n:
            break
        f = dict(zip(range(m), repeat(-1, m)))
        mysum = lambda arr: reduce(lambda x, y: x + y, arr, 0)
        a = list(map(int, input().split()))
        remix = lambda aa: list(starmap(lambda x, mm: fancy_mod(x, mm), zip(aa, repeat(m))))
        a_modm = remix(a)
        nmax = max(a_modm) if a_modm else 0
        tot = mysum(a)
        ans = (lambda A: A[-1] if m > 0 and A else 0)(
            [v for v in a_modm if v == m-1])
        s_accu = list(accumulate(a_modm, lambda x, y: fancy_mod(x + y, m), initial=0))
        for idx, val in enumerate(s_accu[1:], 1):
            f[val] = idx
            s[idx] = val
        if not ans:
            if not nmax:
                ans = 0
            elif tot < m:
                ans = tot
            else:
                span = list(range(m-1, nmax-1, -1))
                def check(ans):
                    # Try all i
                    return any(fancy_mod(s[i]+ans, m) in f and f[fancy_mod(s[i]+ans, m)] >= i for i in range(n+1))
                complex_result = list(dropwhile(lambda an: not check(an), span))
                ans = complex_result[0] if complex_result else 0
        print(ans)

from itertools import dropwhile
orchestrate()