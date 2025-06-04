from functools import reduce
from itertools import permutations, chain, zip_longest, product, combinations
import operator

def split(n, a, b, remain, ai, ans, width, l=None):
    if width == 2:
        list(map(lambda t: ans.__setitem__(t[0], t[1]), enumerate((a, b), start=ai)))
        return
    if l is None:
        x = operator.xor(a, b)
        y = operator.and_(x, -x)
        l = y.bit_length() - 1
    else:
        y = 1 << l
    try:
        remain.remove(l)
    except KeyError:
        pass
    i = next(iter(remain))
    lb = operator.xor(a, 1 << i)
    ra = operator.xor(lb, y)
    width //= 2
    split(n, a, a ^ (1 << i), remain, ai, ans, width, i)
    split(n, ra, b, remain, ai + width, ans, width)
    remain.add(l)

def solve(n, a, b):
    parity = lambda x: reduce(operator.xor, (int(i) for i in bin(x)[2:]), 0)
    if parity(a) == parity(b):
        print('NO')
        return
    remain = set(range(n))
    ans = [0] * (1 << n)
    split(n, a, b, remain, 0, ans, 1 << n)
    print('YES')
    print(*ans)

n, a, b = list(map(int, ''.join(chain.from_iterable(map(str, input().split()))).split()))
solve(n, a, b)