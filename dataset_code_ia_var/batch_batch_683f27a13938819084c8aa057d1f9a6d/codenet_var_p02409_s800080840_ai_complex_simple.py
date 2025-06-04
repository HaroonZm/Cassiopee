from functools import reduce
from operator import add

num = int(input())
get = lambda: list(map(int, input().split()))

buildings = reduce(lambda acc, _: acc + [[[[0]*10 for _ in range(3)]]], range(4), [])[1:]

for _ in range(num):
    b, f, r, v = get()
    reduce(lambda arr, idx: arr[idx-1], [b, f, r], buildings)[0] += v

fstr = lambda x: ' ' + ' '.join(map(str, x))
sep = '#' * 20

print('\n'.join('\n'.join(fstr(fl[0]) for fl in bd) + ('' if i == 3 else f'\n{sep}') for i, bd in enumerate(buildings)))