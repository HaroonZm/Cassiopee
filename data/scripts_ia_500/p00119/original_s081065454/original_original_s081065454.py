from collections import deque
def solve():
    M = int(input())
    G = [[] for i in range(M)]
    deg = [0]*M
    N = int(input())
    for i in range(N):
        x, y = map(int, input().split())
        G[x-1].append(y-1)
        deg[y-1] += 1
    que = deque()
    ans = []
    for i in range(M):
        if deg[i] == 0:
            que.append(i)
    while que:
        v = que.popleft()
        ans.append(v+1)
        for w in G[v]:
            deg[w] -= 1
            if deg[w] == 0:
                que.append(w)
    print(*ans, sep='\n')
solve()