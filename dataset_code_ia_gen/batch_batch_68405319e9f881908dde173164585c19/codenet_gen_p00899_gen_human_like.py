def compute_overlap(a, b):
    max_olap = 0
    min_len = min(len(a), len(b))
    for l in range(min_len, 0, -1):
        if a[-l:] == b[:l]:
            return l
    return 0

def shortest_superstring_length(words):
    n = len(words)
    # Remove words that are substrings of others
    filtered = []
    for w in words:
        if not any(w != other and w in other for other in words):
            filtered.append(w)
    words = filtered
    n = len(words)

    overlap = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                overlap[i][j] = compute_overlap(words[i], words[j])

    full_mask = (1 << n) - 1
    dp = [[float('inf')] * n for _ in range(1 << n)]
    # path reconstruction not needed, only length

    for i in range(n):
        dp[1 << i][i] = len(words[i])

    for mask in range(1 << n):
        for last in range(n):
            if dp[mask][last] == float('inf'):
                continue
            for nxt in range(n):
                if (mask & (1 << nxt)) == 0:
                    new_mask = mask | (1 << nxt)
                    cost = dp[mask][last] + len(words[nxt]) - overlap[last][nxt]
                    if cost < dp[new_mask][nxt]:
                        dp[new_mask][nxt] = cost

    return min(dp[full_mask])

while True:
    n = int(input())
    if n == 0:
        break
    cities = [input().strip() for _ in range(n)]
    print(shortest_superstring_length(cities))