from functools import reduce
from itertools import accumulate, chain, tee

input()
s = input()

# Helper to accumulate growing tuples
def grow(iterable):
    return list(accumulate(iterable, lambda a, b: a + b))

# Generate all first, second, and third order subsequences (contiguous substrings)
g = (lambda seq: (
    set(chain.from_iterable(grow(seq[:i+1]) for i in range(len(seq)))),
    set(chain.from_iterable(
        grow(
            reduce(lambda acc, _: acc[1:], tee(seq, len(seq)))[i][:j+1]
        ) for i in range(len(seq)) for j in range(i+1, len(seq))
    )),
    set()
))

# Simulate the logic of building length-3 substrings ingeniously
def elegant(s):
    # All possible pairs where order is maintained
    pairs = set(chain.from_iterable(
        [(s[i], s[j]) for i in range(len(s)) for j in range(i+1, len(s))]
    ))
    # All possible triplets where order is maintained
    triplets = set(
        ''.join((s[i], s[j], s[k]))
        for i in range(len(s))
        for j in range(i+1, len(s))
        for k in range(j+1, len(s))
    )
    return len(triplets)

print(elegant(s))