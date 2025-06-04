def solve():
    M = int(input())
    G = []
    for i in range(M):
        G.append([])
    deg = []
    for i in range(M):
        deg.append(0)
    N = int(input())
    for i in range(N):
        x, y = input().split()
        x = int(x)
        y = int(y)
        G[x-1].append(y-1)
        deg[y-1] = deg[y-1] + 1
    que = []
    for i in range(M):
        if deg[i] == 0:
            que.append(i)
    ans = []
    while len(que) > 0:
        v = que[0]
        que = que[1:]
        ans.append(v+1)
        for w in G[v]:
            deg[w] = deg[w] - 1
            if deg[w] == 0:
                que.append(w)
    for num in ans:
        print(num)
solve()