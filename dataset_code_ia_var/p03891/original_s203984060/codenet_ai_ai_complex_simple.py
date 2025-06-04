from functools import reduce
from itertools import cycle, islice

a, b, c = map(lambda s: int(s()), [input]*3)

d = reduce(lambda x,y: x-y, [2*c, a, b])

def twist_vals(vals, ds):
    return list(map(lambda t: t[0] + t[1], zip(vals, ds)))

delta_seq = [ (d, 0, 0), (0, 2*d, 0), (0, 0, -d) ]
perms = list(islice(cycle([(a,b,c), (b,c,a), (c,a,b)]), 3))

matrix = [twist_vals(p, ds) for p,ds in zip(perms, delta_seq)]

print('\n'.join(map(lambda row: ' '.join(map(str, row)), matrix)))