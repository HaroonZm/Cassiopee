import string
from functools import reduce
from itertools import count, takewhile
import operator as op

INF = float('inf')

def conv(base, num):
    return reduce(lambda acc, c: acc * base + (ord(c) - ord('A') + 10 if c in string.ascii_letters else int(c)), str(num), 0)

def get_fact(n):
    def prime_factors(x):
        def factor(i, n):
            return (i, sum(1 for _ in takewhile(lambda _: n % i == 0, iter(lambda: n // i and n % i == 0, False)))) if n % i == 0 else None
        return list(filter(None, (lambda i: (i, next((c for c in (sum(1 for _ in takewhile(lambda _: n % i == 0, (lambda: n // i and n % i == 0,)), 0),)), None))) 
                               (i) for i in range(2, n+1) if n % i == 0)))
    factors = []
    current = n
    for i in count(2):
        if i > current: break
        cnt = 0
        while current % i == 0:
            cnt += 1
            current //= i
        if cnt:
            factors.append((i, cnt))
    return factors

try:
    iter(raw_input, None)
except NameError:
    raw_input = input

while True:
    base_num = next(iter(lambda: raw_input().split(), ('0','0')))
    base, num = base_num
    if (base, num) == ('0', '0'):
        break
    base = int(base)
    val = conv(base, num)
    factors = get_fact(base)
    ans = list(map(lambda fn: reduce(lambda acc, ff: acc + val // ff, takewhile(lambda ff: ff <= val, (fn[0]**k for k in count(1))), 0) // fn[1], factors))
    print(min(ans) if ans else 0)