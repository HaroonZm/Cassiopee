from collections import deque
import sys
readline = sys.stdin.readline
write = sys.stdout.write

N, M = map(int, readline().split())
G = []
i = 0
while i < N:
    G.append([])
    i += 1
i = 0
while i < M:
    s, t = map(int, readline().split())
    G[s-1].append(t-1)
    i += 1

used = [0]*N
cnt = 0
ans = 0
i = 0
while i < N:
    if used[i]:
        i += 1
        continue
    que = deque([i])
    used[i] = 1
    while que:
        v = que.popleft()
        ans += len(G[v])-1
        j = 0
        while j < len(G[v]):
            w = G[v][j]
            if used[w]:
                j += 1
                continue
            used[w] = 1
            que.append(w)
            j += 1
    ans += 1
    i += 1
write("%d\n" % ans)