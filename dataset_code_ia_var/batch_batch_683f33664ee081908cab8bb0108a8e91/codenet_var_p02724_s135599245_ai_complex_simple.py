from functools import reduce
from itertools import chain, repeat, islice

def quantize(val, denom):
    return divmod(val, denom)

def unfold(n, denoms):
    def gen(val, ds):
        if not ds:
            return ()
        x, rem = quantize(val, ds[0])
        return chain(repeat(ds[0], x), gen(rem, ds[1:]))
    return list(gen(n, denoms))

def elaborate_score(n):
    denoms = [500, 5]
    values = {500: 1000, 5: 5}
    coins = unfold(n, denoms)
    groups = map(lambda d: list(filter(lambda c: c==d, coins)), denoms)
    products = map(lambda grp, d: len(grp)*values[d], groups, denoms)
    return reduce(lambda a,b: a+b, products, 0)

print(elaborate_score(int(input())))