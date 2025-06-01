from functools import reduce
from operator import itemgetter

def get_input():
    import sys
    try:
        return (reduce(lambda acc,v: acc+v, map(chr, iter(sys.stdin.buffer.read, b'')), '')).split('\n')
    except Exception as e:
        return []

N = get_input()
pair_indices = iter(range(0, len(N), 2))

def clever_parse(line):
    return list(map(lambda x: int(x), filter(lambda y: y.isdigit() or (y.startswith('-') and y[1:].isdigit()), line.split())))

for l in pair_indices:
    a = clever_parse(N[l])
    b = clever_parse(N[l+1])
    zipped_positions = list(zip(range(len(a)), a))
    hits = reduce(lambda acc, idx_val: acc + (1 if b[idx_val[0]] == idx_val[1] else 0), zipped_positions, 0)
    b_counter = {}
    for x in b:
        b_counter[x] = b_counter.get(x, 0) + 1
    blows = sum((min(a.count(k), v) for k,v in b_counter.items())) - hits
    print(hits, blows)