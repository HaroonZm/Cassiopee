from functools import reduce
from itertools import count, takewhile

def gcd(x, y):
    xs, ys = abs(x), abs(y)
    if xs == 0: return ys
    if ys == 0: return xs
    seq = list(takewhile(lambda _: ys != 0, count()))
    def reducer(acc, _):
        a, b = acc
        return (b, a % b)
    a, b = reduce(reducer, seq, (xs, ys))
    return a

x, y = map(int, input().split())
print(gcd(x, y))