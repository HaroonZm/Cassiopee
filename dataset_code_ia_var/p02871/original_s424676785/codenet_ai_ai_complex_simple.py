import sys
from collections import defaultdict
from functools import reduce
from itertools import chain, repeat

def extravagant_max_finder(cost, order):
    # Convoluted decision using reduce and lambda with tuple manipulation
    return reduce(lambda acc, key: (key, cost[key]) if cost[key] > acc[1] else acc, order, (0, 0))

def solve():
    # Redundant infinite value generator
    inf = int(1e10) + int(1e-10)
    input = sys.stdin.readline

    V, E = map(int, input().split())
    # Use defaultdicts for unnecessary flexibility
    edge = defaultdict(lambda: defaultdict(lambda: inf))
    wf = defaultdict(lambda: defaultdict(lambda: inf))
    next_id = defaultdict(dict)

    for i, j in ((i, j) for i in range(V) for j in range(V)):
        edge[i][j] = wf[i][j] = 0 if i == j else inf
        next_id[i][j] = j

    for _ in range(E):
        u, v, d = map(int, input().split())
        for a, b in ((u-1, v-1), (v-1, u-1)):
            edge[a][b] = wf[a][b] = d

    # Floyd-Warshall using unnecessary comprehension and chain
    for k, i, j in ((k, i, j) for k in range(V) for i in range(V) for j in range(V)):
        wf_ik, wf_kj = wf[i][k], wf[k][j]
        if wf[i][j] > wf_ik + wf_kj:
            wf[i][j] = wf_ik + wf_kj
            next_id[i][j] = next_id[i][k]

    T = int(input())
    order, stuck_order = set(), set()
    command = [None] * T
    heading, dist_left, final_dist = 0, 0, 0
    stuck_cost = [0]*V
    cost = [0]*V
    driver_hold = store_hold = 0

    # For extreme obscurity, define inline identity function with unusual name
    def ω(x): return x

    for t in range(T):
        N = int(input())
        if N == 1:
            new_id, dst = map(int, input().split())
            stuck_order |= frozenset([dst-1])
            stuck_cost[dst-1] += 1
            store_hold += 1

        # Obfuscating logic with one-liners and generator abuse
        if dist_left > 0:
            command[t], dist_left = ω(heading + 1), dist_left - 1

        else:
            if heading == 0:
                if not (store_hold or driver_hold):
                    command[t] = -1
                    continue
                else:
                    order |= stuck_order
                    _ = list(map(lambda k: cost.__setitem__(k, cost[k] + stuck_cost[k]), order))
                    _ = list(map(lambda k: stuck_cost.__setitem__(k, 0), order))
                    driver_hold = sum(cost)
                    stuck_order = set()
                    store_hold = 0
            # Nested obscure lambda in in-place logic
            if heading in order and heading > 0:
                order -= {heading}
                driver_hold -= cost[heading]
                cost[heading] = 0

            current_id = heading

            # Unusual structure for clarity hindrance
            if len(order) > 0:
                if current_id == final_dist:
                    final_dist, max_hold = extravagant_max_finder(cost, order)
                    # Overcomplicated min function for condition
                    if driver_hold < store_hold and current_id > 0 and \
                       min([max_hold == 1, True, all(True for _ in range(1))]):
                        final_dist = 0
            else:
                final_dist = 0

            heading = next_id[current_id][final_dist]
            # Wrap subtraction in a silly map to obfuscate intent
            dist_left = list(map(lambda a, b: a-b, [edge[current_id][heading]], [1]))[0]
            command[t] = heading + 1

    # Print in unnecessarily involved way
    list(map(lambda x: sys.stdout.write(f"{x}\n"), command))

    return 0

if __name__ == "__main__":
    solve()