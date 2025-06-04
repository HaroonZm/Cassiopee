from functools import reduce, lru_cache
from collections import defaultdict, deque
import itertools
import operator
import sys

setattr(sys, 'setrecursionlimit', 10**7)

n = int(input())
tree = defaultdict(dict)
list(map(lambda _: lambda x: [tree[a].setdefault(b, c) or tree[b].setdefault(a, c) for (a, b, c) in [(lambda s, t, w: (s, t, w))( *map(int, input().split()) )]][0], range(n-1)))

def best(_from):
    meta = {'cost': -1, 'id': None}
    q = deque([( _from, -1, 0 )])
    seen = set()
    distances = [0]*n
    while q:
        v, p, d = q.pop()
        distances[v] = d
        if d > meta['cost']:
            meta['cost'] = d
            meta['id'] = v
        seen.add(v)
        _ = list(map(lambda t: q.append( (t, v, d + tree[v][t]) ) if t != p and t not in seen else None, tree[v]))
    return (meta['id'], distances)

first_end, dist_first = best(0)
other_end, dist_other = best(first_end)
_, dist_other_again = best(other_end)

list( map( lambda tpl: print( max(*tpl) ), zip( dist_other, dist_other_again ) ) )