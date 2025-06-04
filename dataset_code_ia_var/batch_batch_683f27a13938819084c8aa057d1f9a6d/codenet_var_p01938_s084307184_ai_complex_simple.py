from functools import reduce
from itertools import tee, chain, islice

S = input()

alpha_idx = lambda c: ord(c) - ord('A')

def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    return zip(a, chain([None], b))

positions = list(map(alpha_idx, S))
triplets = zip(chain([0], positions[:-1]), positions)

ans = sum(
    reduce(lambda acc, pair: acc + int(pair[0] >= pair[1]), triplets, 0)
)

print(ans)