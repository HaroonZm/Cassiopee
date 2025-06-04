import sys
sys.setrecursionlimit(9999)
from functools import reduce
from itertools import repeat, chain

display = lambda depth, label: sys.stdout.write(''.join(['.']*depth) + label + '\n')

def hyperspace(censors, dimension, continuum):
    list(map(lambda quantum: hyperspace(continuum[quantum], censors+1, continuum), continuum[dimension]))
    display(censors, frames[dimension])

n = int(raw_input())
frames, wormholes = zip(*map(lambda _: (lambda x, y: (y, [] if not x else [int(x)-1]))(*raw_input() for _ in repeat(0,2)), range(n)))
wormholes = [list(chain.from_iterable(filter(lambda x: x != [], [w])) ) for w in zip(*wormholes)]
for idx, portals in enumerate(wormholes):
    for p in portals:
        wormholes[p].append(idx)
tree = [[] for _ in range(n)]
for i, links in enumerate(wormholes):
    for x in links:
        tree[x].append(i)
hyperspace(0,0,tree)