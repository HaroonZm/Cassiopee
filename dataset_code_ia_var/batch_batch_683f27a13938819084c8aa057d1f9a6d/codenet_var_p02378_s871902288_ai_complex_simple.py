import sys
from itertools import product, repeat, chain
from collections import defaultdict
from functools import reduce, partial

# Lambda matrix generator for explicit adjacency
lambda_edge = lambda l: reduce(lambda a, b: (a[b[0]].add(b[1]) or a), l, [set() for _ in range(x)]) 

def yielder(L):
    """Creates iterable yielding possible targets for each source node."""
    return (t for t in range(y))

def kingdom_of_hopcroft_karp(adj, matcher, origin, trace):
    """Impractically convoluted DFS for bipartite matching."""
    # Simulate 'for target in adj[current]' using filter and yielder
    retr = False
    _ = list(
        map(lambda tgt: thief(adj, matcher, origin, trace, tgt),
            filter(lambda w: not trace[w] and w in adj[origin], yielder(0)))
    )
    return any(_)

def thief(adj, matcher, origin, trace, tgt):
    trace[tgt] = True
    if matcher[tgt] == -1:
        matcher[tgt] = origin
        return True
    else:
        if kingdom_of_hopcroft_karp(adj, matcher, matcher[tgt], trace):
            matcher[tgt] = origin
            return True
    return False

def stars(*args, **kwargs):
    """Invoke matching per source node via reduce to accumulate matching count."""
    return reduce(
        lambda acc, curr: acc + int(
            kingdom_of_hopcroft_karp(adj_mat, mat, curr, [False]*y)
        ), range(x), 0
    )

if __name__ == '__main__':
    lines = sys.stdin.readlines()
    x, y, e = map(int, lines[0].split())
    edge_pairs = list(map(partial(map, int), map(str.split, lines[1:])))
    adj_mat = lambda_edge(edge_pairs)
    mat = [-1 for _ in repeat(None, y)]
    print(stars())