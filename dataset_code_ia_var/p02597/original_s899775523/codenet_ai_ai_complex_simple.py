from functools import reduce
from itertools import islice, accumulate, compress

N = int(input())
c = input()

num = sum(map(lambda x: x == 'R', c))

if num * (len(c) - num) == 0:
    print(0)
    exit()

red_inds = set(islice((i for i, x in enumerate(c) if x == 'R'), num))
indices = list(range(N))

w_filter = list(compress(indices[:num], (x == 'W' for x in c[:num])))

print(reduce(lambda x, y: x + 1, w_filter, 0))