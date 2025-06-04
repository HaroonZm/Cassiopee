from functools import reduce
from itertools import starmap, repeat

t = list(map(lambda c: c, input()))

def replace_question(idx_c_tuple):
    idx, c = idx_c_tuple
    return (lambda y: y if y != '?' else 'D')(c)

t = list(starmap(lambda idx, c: replace_question((idx, c)), enumerate(t)))

print(reduce(lambda acc, x: acc + x, t, ""))