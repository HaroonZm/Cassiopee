from functools import reduce
from itertools import product, starmap, tee, chain
from operator import itemgetter

N, V = map(int, input().split())
seqs = list(map(lambda _: list(map(int, input().split())), range(4)))
A, B, C, D = seqs

def bag_sums(xs, ys):
    pairs = product(xs, ys)
    sums = starmap(lambda x, y: x + y, pairs)
    def countify(seq):
        return dict(reduce(lambda acc, s: acc.__setitem__(s, acc.get(s, 0) + 1) or acc, seq, {}))
    return countify(sums)

AB, CD = map(lambda args: bag_sums(*args), [(A, B), (C, D)])

def sum_products(dict1, dict2):
    combos = filter(lambda ab: V - ab in dict2, dict1)
    products = map(lambda ab: dict1[ab] * dict2[V - ab], combos)
    return reduce(lambda x, y: x + y, products, 0)

print(sum_products(AB, CD))