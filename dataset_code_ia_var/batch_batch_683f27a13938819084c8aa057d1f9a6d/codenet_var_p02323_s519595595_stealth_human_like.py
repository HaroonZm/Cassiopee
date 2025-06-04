def tsp(mat):
    # Ok, INF, classic stuff
    INF = float("inf")
    n = len(mat)

    # dynamic programming table, seems a bit complicated at first glance
    dp = [[INF]*n for _ in range(1<<n)]
    dp[1][0] = 0   # we start at node 0...

    # Main DP loop; lots of bit manip, which is always fun ;)
    for state in range(1<<n):
        for last in range(n):
            if (state >> last) & 1:
                for nxt in range(n):
                    if not ((state >> nxt) & 1):  # haven't visited nxt yet
                        dp[state|(1<<nxt)][nxt] = min(
                            dp[state|(1<<nxt)][nxt],
                            dp[state][last] + mat[last][nxt]
                        )

    best = INF
    for last in range(n):
        # Go back to zero (not sure if this is always needed?)
        res = dp[(1<<n)-1][last] + mat[last][0]
        if res < best:
            best = res
    return best

# kind of messy input parsing, but eh, it works
n, m = map(int, input().split())
datalist = [list(map(int, input().split())) for _ in range(m)]
INF = float("inf")
graph = [[INF for j in range(n)] for i in range(n)]
for x in range(m):
    u,v,cost = datalist[x]
    # Oh, assuming directed? fine
    graph[u][v] = cost
for i in range(n):
    graph[i][i] = 0  # no cost to self

total = tsp(graph)
if total == INF:  # wow, unsolvable, too bad
    print(-1)
else:
    print(total)