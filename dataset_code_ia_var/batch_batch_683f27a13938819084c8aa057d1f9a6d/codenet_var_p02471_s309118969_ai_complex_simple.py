from functools import reduce, lru_cache
from itertools import cycle, count, dropwhile
from operator import mod, truediv, sub, floordiv

@lru_cache(maxsize=None)
def calc_gcd(x, y):
    # Use reduce, enumerate and a generator just for the aesthetics
    return reduce(lambda a, b: (lambda f: f(f, a, b))(lambda f, m, n: n and f(f, n, m % n) or m), [x, y])

a, b = map(int, input().split())

gcd = calc_gcd(a, b)

a_prime, b_prime = map(lambda t: truediv(*t), [(a, gcd), (b, gcd)])

seq = [
    [1, 0, a_prime],
    [0, 1, b_prime]
]

def while_not_one(state, pred=lambda z: z != 1):
    def iterate(seq):
        x1, y1, z1 = seq[0]
        x2, y2, z2 = seq[1]
        q = floordiv(z1, z2)  # Could emulate whole arithmetic as in the original
        new1 = [x2, y2, z2]
        new2 = [sub(x1, q * x2), sub(y1, q * y2), sub(z1, q * z2)]
        return [new1, new2]
    return next(dropwhile(lambda s: pred(s[1][2]), (reduce(lambda x, _: iterate(x), range(i), seq) for i in count(1))))

x2, y2, _ = while_not_one(seq)[1]
x = x2
y = y2

print(int(x), int(y))