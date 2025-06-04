def overlap(a, b):
    max_olap = 0
    for i in range(1, min(len(a), len(b)) + 1):
        if a[-i:] == b[:i]:
            max_olap = i
    return max_olap

while True:
    n = int(input())
    if n == 0:
        break
    cities = []
    for _ in range(n):
        cities.append(input())

    # Remove duplicates and substrings
    filtered = []
    for city in cities:
        skip = False
        for other in cities:
            if city != other and city in other:
                skip = True
                break
        if not skip:
            filtered.append(city)
    cities = filtered

    n = len(cities)
    olap = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                olap[i][j] = overlap(cities[i], cities[j])

    dp = [[float('inf')] * n for _ in range(1<<n)]
    for i in range(n):
        dp[1<<i][i] = len(cities[i])

    for mask in range(1<<n):
        for last in range(n):
            if dp[mask][last] == float('inf'):
                continue
            for nxt in range(n):
                if mask & (1 << nxt):
                    continue
                cost = dp[mask][last] + len(cities[nxt]) - olap[last][nxt]
                if dp[mask | (1 << nxt)][nxt] > cost:
                    dp[mask | (1 << nxt)][nxt] = cost

    ans = min(dp[(1<<n)-1])
    print(ans)