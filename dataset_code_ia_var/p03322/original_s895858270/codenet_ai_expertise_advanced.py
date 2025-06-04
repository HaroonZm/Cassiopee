import random
from collections import defaultdict
from itertools import accumulate
from operator import itemgetter

def solve(n, s, xs, m):
    ans = [float('inf')] * (n + 1)
    s2val = {'>': 1, '<': -1, '+': 0, '-': 0}
    op2func = {'+': lambda h, y, m: (h + y) % m, '-': lambda h, y, m: (h - y) % m}

    for x in xs:
        y = 1
        r = pow(x, m - 2, m)
        pos = [0]
        hashes = [0]
        p = h = 0

        for c in s:
            if c in ('>', '<'):
                p += s2val[c]
                y = y * (x if c == '>' else r) % m
            else:
                h = op2func[c](h, y, m)
            pos.append(p)
            hashes.append(h)

        pmin, pmax = min(pos), max(pos)
        pow_x = [1]
        if pmin < 0:
            pow_x += list(accumulate([x] * (pmax - pmin), lambda a, b: a * b % m, initial=pow(r, -pmin, m)))
        else:
            pow_x += list(accumulate([x] * pmax, lambda a, b: a * b % m))
        pow_x = [pow_x[p - pmin] for p in range(pmin, pmax + 1)]

        ideal = hashes[-1]
        required = defaultdict(int)
        for i, (p, h) in enumerate(zip(pos, hashes)):
            ans[i] = min(ans[i], required[h])
            req = (ideal * pow_x[p - pmin] + h) % m
            required[req] += 1

    return sum(ans)

n = int(input())
s = input()
xs = random.sample(range(10 ** 9, 10 ** 10), 3)
m = 2305843009213693951
print(solve(n, s, xs, m))