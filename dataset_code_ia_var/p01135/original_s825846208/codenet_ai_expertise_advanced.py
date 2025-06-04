from sys import stdin
from itertools import repeat, chain
from heapq import heappop, heappush

def solve():
    inf = 310001  # 10000 * 31 + 1

    def warshall_floyd(n, dist, next_p):
        for k, i, j in ((k, i, j) for k in range(n) for i in range(n) for j in range(n)):
            d = dist[i][k] + dist[k][j]
            if d < dist[i][j]:
                dist[i][j] = d
                next_p[i][j] = next_p[i][k]
            elif k != i and d == dist[i][j] and next_p[i][k] < next_p[i][j]:
                next_p[i][j] = next_p[i][k]

    def reconstruct_path(next_p, s, t):
        path = [s]
        while s != t:
            s = next_p[s][t]
            path.append(s)
        return path

    lines = iter(stdin)
    append_ans = []
    while True:
        try:
            n, m = map(int, next(lines).split())
        except StopIteration:
            break
        if n == 0:
            break

        dist = [[0 if i == j else inf for j in range(n)] for i in range(n)]
        for _ in range(m):
            s, t, d = map(int, next(lines).split())
            dist[s - 1][t - 1] = dist[t - 1][s - 1] = d

        next_p = [list(range(n)) for _ in repeat(None, n)]
        warshall_floyd(n, dist, next_p)

        l = int(next(lines))
        info = [next(lines).split() for _ in range(l)]
        starts, goals, ats, msgs = zip(*info)
        starts = [int(x)-1 for x in starts]
        goals = [int(x)-1 for x in goals]
        ats = list(map(int, ats))
        steps = [1]*l
        paths = [reconstruct_path(next_p, s, g) for s, g in zip(starts, goals)]

        mails = []
        for i, (at, path) in enumerate(zip(ats, paths)):
            if len(path) > 1:
                heappush(mails, (at, at, path[1], path[0], i))

        deliv_time = [0]*n
        res = []

        while mails:
            t, at, nxt, cur, idx = heappop(mails)
            # Aggregate all mails at this time, cur, nxt
            group = [(t, at, nxt, cur, idx)]
            while mails and mails[0][:4] == (t, at, nxt, cur):
                group.append(heappop(mails))

            dt = deliv_time[cur]
            if t >= dt:
                cost = dist[cur][nxt]
                new_t = t + cost
                for _, _, nxt, cur, num in group:
                    if nxt == goals[num]:
                        res.append((new_t, msgs[num]))
                    else:
                        steps[num] += 1
                        new_nxt = paths[num][steps[num]]
                        heappush(mails, (new_t, new_t, new_nxt, nxt, num))
                deliv_time[cur] = t + 2 * cost
            else:
                for _, orig_at, nxt, cur, num in group:
                    heappush(mails, (dt, orig_at, nxt, cur, num))

        res.sort()
        append_ans.extend((f"{label} {time}" for time, label in res))
        append_ans.append("")

    print('\n'.join(append_ans).rstrip())

solve()