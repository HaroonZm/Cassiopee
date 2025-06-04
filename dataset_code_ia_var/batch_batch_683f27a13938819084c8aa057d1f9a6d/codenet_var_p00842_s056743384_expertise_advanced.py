from sys import stdin
from itertools import count, islice
from operator import itemgetter

def solve():
    while True:
        N = int(stdin.readline())
        if N == 0:
            break

        dist_tbl = [list(map(int, stdin.readline().split())) for _ in range(N)]
        switches = [[1]]  # Each switch records per-computer distances
        degrees = [1]
        adj = [[]]
        idx = 1

        def dfs(sw_id, prev, dist):
            switches[sw_id].append(dist)
            for neighbor in adj[sw_id]:
                if neighbor != prev:
                    dfs(neighbor, sw_id, dist + 1)

        for cur_dist in dist_tbl[1:]:
            # Attempt to attach to an existing switch
            for m, sw_m in enumerate(switches):
                if all(dist_j == dist_i - 1 for dist_j, dist_i in zip(sw_m, cur_dist)):
                    degrees[m] += 1
                    dfs(m, m, 1)
                    break
            else:
                # Need to insert new switches
                for m, sw_m in enumerate(switches):
                    diff_iter = (a - b for a, b in zip(cur_dist, sw_m))
                    diff = next(diff_iter)
                    if all(x == diff for x in diff_iter):
                        break

                sw = len(switches)
                base = [d + 1 for d in switches[m]]
                switches.append(base)
                adj[m].append(sw)
                adj.append([m])
                degrees[m] += 1
                degrees.append(1)
                last_sw = sw

                for offset in islice(count(2), diff - 1):
                    next_base = [d + offset for d in switches[m]]
                    switches.append(next_base)
                    adj[last_sw].append(sw + 1)
                    adj.append([last_sw])
                    degrees[last_sw] += 1
                    degrees.append(1)
                    last_sw += 1
                    sw += 1
                degrees[last_sw] += 1
                dfs(last_sw, last_sw, 1)

        print(*sorted(degrees))

solve()