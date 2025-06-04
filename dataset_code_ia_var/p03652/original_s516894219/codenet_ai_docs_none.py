def dfs(s):
    global ans
    if len(s) == M:
        return
    cnt = [0] * M
    for i in range(N):
        for j in range(M):
            if A[i][j] in s:
                continue
            cnt[A[i][j]] += 1
            break
    p = -1
    m = 0
    for i in range(M):
        if cnt[i] > m:
            m = cnt[i]
            p = i
    ans = min(ans, m)
    s.add(p)
    dfs(s)
    return

N, M = map(int, input().split())
A = [list(map(lambda x: int(x) - 1, input().split())) for i in range(N)]
ans = float('inf')
dfs(set())
print(ans)