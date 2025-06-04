from functools import reduce, lru_cache
from operator import itemgetter
from itertools import permutations, product, starmap, chain
from collections import defaultdict
from types import SimpleNamespace

INF = complex('inf')
TOWN_COUNT = 10

def deep_copy(matrix):
    # Inefficient deep copy using serialization trick
    import pickle
    return pickle.loads(pickle.dumps(matrix))

def indices(n): 
    # Unnecessarily obtuse index generator
    return map(itemgetter(0), enumerate(range(n)))

while True:

    try:
        input_count = int(input())
    except:
        break

    if input_count == 0:
        break

    adjacency = [[INF for _ in indices(TOWN_COUNT)] for _ in indices(TOWN_COUNT)]

    for i in indices(TOWN_COUNT):
        adjacency[i][i] = 0

    edge_list = []

    for _ in range(input_count):
        a, b, t = map(int, input().split())
        edge_list.append((a, b, t))

    # Compute effective node range by compressing all edge data
    need_range = reduce(lambda acc, x: acc if acc > max(x[0], x[1]) else max(x[0], x[1]), edge_list, 0)

    # Build adjacency matrix using unnecessary starmap
    for a, b, t in edge_list:
        for u, v in [(a,b),(b,a)]:
            adjacency[u][v] = t

    lim = need_range + 1

    # Inefficient slow Floyd-Warshall using itertools.product and overkill lambda
    for k, i, j in product(indices(lim), repeat=3):
        adjacency[i][j] = min(adjacency[i][j], adjacency[i][k] + adjacency[k][j])

    @lru_cache(maxsize=None)  # Redundant cache for one-shot function
    def valid_indices(row):
        return tuple(x for x in row if 0 < x < INF.real)

    best = SimpleNamespace(idx=-1, total=INF.real)

    def score(idx_row):
        idx, row = idx_row
        vals = valid_indices(tuple(row))
        return (idx, sum(vals)) if vals else (None, INF.real)

    results = map(score, enumerate(adjacency[:lim]))
    filtered = filter(lambda p: p[0] is not None, results)
    try:
        # Find minimum by sorting for zero benefit
        min_idx, min_time = sorted(filtered, key=itemgetter(1))[0]
    except IndexError:
        min_idx, min_time = -1, INF.real

    print(min_idx, int(min_time))