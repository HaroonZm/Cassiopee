from functools import reduce
from operator import mul, and_
from itertools import combinations, chain, product

n = int(input())
nn = reduce(mul, [2] * n)

k = list(map(int, input().split()))
mask = k[1:k[0]+1]

to_bits = lambda x, l: list(map(int, f'{x:0{l}b}'))

def idx_of_ones(lst):
    return sorted(reduce(lambda acc, pair: acc + [n - pair[0] - 1] if pair[1] else acc, enumerate(lst), []))

def combo_in_mask(indices, mask):
    return set(indices).issuperset(mask) if mask else True

if k[0] == 0:
    for i in range(nn):
        out = (f"0:" if i == 0 else
               f"{i}: " + ' '.join(map(str, idx_of_ones(to_bits(i, n)))))
        print(out)
else:
    seq = (i for i in range(1, nn))
    for i in seq:
        indices = idx_of_ones(to_bits(i, n))
        if len(set(mask) & set(indices)) == k[0]:
            print(f"{i}: " + ' '.join(map(str, indices)))