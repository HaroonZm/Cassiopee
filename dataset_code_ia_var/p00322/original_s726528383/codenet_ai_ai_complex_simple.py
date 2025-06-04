from functools import reduce
from operator import add, itemgetter
from itertools import permutations, compress, chain

a = list(input().split())
b = set(map(str, range(1, 10)))
indices = list(range(9))
present = set(a)
remaining = b - present
missing_indices = [i for i in indices if a[i] not in b]

# Build a mask for positions needing values
mask = list(map(lambda x: x in missing_indices, indices))
positions = tuple(compress(indices, mask))

flatten = lambda l: list(chain.from_iterable(l))
assign = lambda x, idxs, vals: reduce(lambda arr, pair: (arr.__setitem__(pair[0], pair[1]), arr)[1], zip(idxs, vals), x)

# Main count
count = sum(
    int(
        int(x[0])
        + int(''.join(x[1:3]))
        + int(''.join(x[3:6])) == int(''.join(x[6:]))
    )
    for perm in permutations(remaining)
    for x in [assign(a[:], positions, perm)]
)
print(count)