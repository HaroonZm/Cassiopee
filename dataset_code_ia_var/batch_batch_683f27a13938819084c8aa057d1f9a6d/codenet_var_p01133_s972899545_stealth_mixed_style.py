def solve():
    import math
    import sys

    class DFS:
        @staticmethod
        def explore(current, to_visit, time, dist_func, time_limits, graph):
            # Fonctionne de façon itérative et récursive selon le cas
            if len(to_visit) == 0:
                return 1
            queued = []
            for nxt in to_visit:
                nxt_time = time + graph[current][nxt]
                if nxt_time < time_limits[nxt]:
                    queued.append((nxt, nxt_time))
                else:
                    # style early return à la C
                    return False
            for selected, acc_time in queued[::-1]:
                # Backtracking façon imperative
                x = set(to_visit)
                x.remove(selected)
                if DFS.explore(selected, x, acc_time, dist_func, time_limits, graph):
                    return True
            return False

    def dist(a, b):
        # style flat functional
        return math.hypot(a[0]-b[0], a[1]-b[1])

    get_input = sys.stdin.readline
    while 1:
        vals = get_input().split()
        # mix index access et unpacking
        if int(vals[0]) == 0: break
        n, hx, hy, dx, dy = [int(x) for x in vals]
        coords = []
        i = 0
        while i < n:
            coords.append(tuple(map(int, get_input().split())))
            i += 1
        # usage comprehensions
        deadlines = [dist((cx,cy), (dx,dy)) for (cx,cy) in coords]
        coords.append((hx, hy))
        # style for+range
        adj = []
        for i in range(n+1):
            row = []
            for j in range(n+1):
                row.append(dist(coords[i], coords[j]))
            adj.append(row)
        # combos de set et range
        if DFS.explore(n, {z for z in range(n)}, 0, dist, deadlines, adj) == 1:
            print('YES')
        else:
            print('NO')
solve()