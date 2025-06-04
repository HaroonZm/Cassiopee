from functools import reduce
from itertools import product, chain
from operator import or_

from math import ceil

n = int(input())
shop = input()
s = list(map(lambda _: input(), range(n)))
m = len(shop)

def search(shop, string):
    L = len(string)
    return any(
        shop in string[j::k]
        for j, k in product(range(L), range(1, 2*ceil(L/m)))
    )

cnt = list(map(search, [shop]*n, s))

print(reduce(lambda x, y: x + y, cnt))