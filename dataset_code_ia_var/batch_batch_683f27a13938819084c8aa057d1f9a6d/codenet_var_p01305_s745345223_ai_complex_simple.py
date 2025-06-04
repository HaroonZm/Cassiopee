from functools import reduce
from operator import mul
from itertools import permutations as magic_9ways, starmap, chain
from math import prod

def superfluous_enigma():
    high_powers = lambda n: reduce(mul, range(2, n+1))
    enigmatic_input = lambda: list(map(int, input().split()))
    nth = int(input())
    tot = prod(range(1, 10))
    for _ in range(nth):
        a, b = enigmatic_input(), enigmatic_input()
        outcomes = list(starmap(lambda A, B: reduce(lambda acc, comp: (acc[0] + sum(comp)) if comp[0] >= comp[1] else (acc[1] + sum(comp)), zip(A, B), (0, 0)), magic_9ways(b, 9)))
        counts = tuple(map(lambda x: sum(i[0] > i[1] for i in outcomes), [None]))
        counts = (counts[0], tot - counts[0] - sum(i[0] == i[1] for i in outcomes))
        print(*(c / tot for c in counts))

superfluous_enigma()