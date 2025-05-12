n = int(input())
ab = [tuple(map(int, input().split())) for _ in range(n)]
cd = [tuple(map(int, input().split())) for _ in range(n)]

gr = {i:[] for i in range(2 * n)}
for i in range(n):
    ai, bi = ab[i]
    for j in range(n):
        cj, dj = cd[j]
        if ai < cj and bi < dj:
            gr[i].append(n + j)
            gr[n + j].append(i)

ans = 0
ab = list(reversed(sorted(ab)))
cd = list(sorted(cd))
used = [False for _ in range(2 * n)]
match = [-1 for _ in range(2 * n)]

def dfs(v):
    global used, n, gr, match
    used[v] = True
    for u in gr[v]:
        w = match[u]
        if w < 0 or (not used[w] and dfs(w)):
            match[v] = u
            match[u] = v
            return True
    return False

for v in range(2 * n):
    if match[v] < 0:
        used = [False for _ in range(2 * n)]
        if dfs(v):
            ans += 1

print(ans)