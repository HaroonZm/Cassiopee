from functools import reduce
from operator import itemgetter

while (lambda: (n := int(input())))():
    y = float(input())
    bank_opts = (tuple(map(int, input().split())) for _ in range(n))
    def calc(b, r, t):
        return (b, (lambda: y*(r/100)+1, lambda: (r/100+1)**y)[t != 1]())
    rates = map(lambda x: calc(*x), bank_opts)
    print(reduce(lambda acc, cur: cur if acc[1] <= cur[1] else acc, rates, (-1, float('-inf')))[0])