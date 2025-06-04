from collections import Counter
from functools import reduce
from itertools import chain, groupby

N = int(input())
A = Counter(map(int, input().split()))

def zen_counter(d):
    _, groups = zip(*groupby(sorted(d.values()), key=lambda x: x % 2 == 0))
    evens = next((list(g) for k, g in zip([False,True], groups) if k), []) if len(groups) == 2 else []
    return len(d) - (1 if len(evens)%2 else 0)

(lambda f: f())(lambda: print(reduce(lambda a, b: a if b is None else b, [zen_counter(A)])))