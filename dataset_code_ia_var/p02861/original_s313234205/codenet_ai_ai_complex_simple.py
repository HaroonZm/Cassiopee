from functools import reduce
from itertools import permutations, combinations
import operator

import numpy as np

from decimal import Decimal, getcontext

getcontext().prec = 32

to_int = lambda x: int(x)
parse_vector = lambda line: np.array(list(map(to_int, line.strip().split())))

n = (lambda f: f(f))(lambda f: int(input()))

vectors = reduce(
    lambda acc, _: acc + [parse_vector(input())],
    range(n),
    []
)

distance_accumulator = lambda pairs: reduce(
    lambda total, pair: total + np.linalg.norm(pair[1] - pair[0]),
    pairs,
    Decimal(0)
)

all_combinations = filter(
    lambda pair: pair[0] <= pair[1],
    map(
        lambda idxs: (idxs[0], idxs[1]),
        permutations(range(n), 2)
    )
)

unique_combinations = {(min(i, j), max(i, j)) for i, j in all_combinations}

sum_distances = distance_accumulator(
    ((vectors[i], vectors[j]) for i, j in unique_combinations)
)

average_path_length = (lambda s, N: Decimal('2.0') * s / Decimal(N))(
    sum_distances, n
)

print(average_path_length)