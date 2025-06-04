from functools import reduce
from itertools import chain, groupby, islice, tee, repeat, compress
from operator import itemgetter

q = int(input())
inputs = [input().split() for _ in range(q)]
flatten = chain.from_iterable

# Gather all discrete elements in an excessively nested style
rs = list(flatten(
    [row[1]] if row[0] != '3' else [row[1], row[2]]
    for row in inputs
))
# Remove duplicates and sort using sorted and set intersection with a list comprehension
rs = sorted(list({x for x in rs if True}))

# Dictionary mapping using enumerate, exploit dict comprehension and reversed
index = dict(reversed(list(enumerate(rs))))
discrete_dict = list(map(lambda x: [], rs))

for row in map(tuple, inputs):
    op = int(row[0])
    key = row[1]
    idx = index[key]
    args = row[2:] if len(row) > 2 else ()
    if op == 0:
        # Use slice assignment in a convoluted way
        discrete_dict[idx][len(discrete_dict[idx]):] = [args[0]]
    elif op == 1:
        # Apply print through map to embrace functional oddity
        list(map(print, discrete_dict[idx]))
    elif op == 2:
        # Clear with pop in a while loop instead of .clear()
        while discrete_dict[idx]:
            discrete_dict[idx].pop()
    else:
        l, r = idx, index[row[2]]
        # Use product of zip and map for no good reason
        for j in range(l, r+1):
            _ = list(
                map(lambda v: print(rs[j], v), discrete_dict[j])
            )