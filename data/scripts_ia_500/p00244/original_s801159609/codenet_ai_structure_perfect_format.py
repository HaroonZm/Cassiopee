def solve():
    from sys import stdin
    from heapq import heappush, heappop

    f_i = stdin

    while True:
        n, m = map(int, f_i.readline().split())
        if n == 0:
            break

        adj = [[] for _ in range(n)]
        for _ in range(m):
            a, b, c = map(int, f_i.readline().split())
            a -= 1
            b -= 1
            adj[a].append((b, c))
            adj[b].append((a, c))

        fare = [[100000] * 3 for _ in range(n)]
        fare[0][2] = 0
        hq = [(0, 0, 2)]  # (fare, pos, remaining ticket)
        target = n - 1

        while hq:
            f1, u, rt = heappop(hq)

            if rt != 1 and u == target:
                print(f1)
                break

            for v, f2 in adj[u]:
                if rt == 0:
                    f3 = f1 + f2
                    if f3 < fare[v][0]:
                        fare[v][0] = f3
                        heappush(hq, (f3, v, 0))
                elif rt == 1:
                    if f1 < fare[v][0]:
                        fare[v][0] = f1
                        heappush(hq, (f1, v, 0))
                else:
                    f3 = f1 + f2
                    if f3 < fare[v][2]:
                        fare[v][2] = f3
                        heappush(hq, (f3, v, 2))
                    if f1 < fare[v][1]:
                        fare[v][1] = f1
                        heappush(hq, (f1, v, 1))


solve()