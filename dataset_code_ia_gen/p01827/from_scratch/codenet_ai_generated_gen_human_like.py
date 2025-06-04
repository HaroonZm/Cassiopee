import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
c = list(map(int, input().split()))
M = int(input())

g = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

p = [1]*N
visited = [False]*N

def dfs(cur):
    visited[cur] = True
    for nxt in g[cur]:
        if c[nxt] > c[cur]:
            if p[nxt] <= p[cur]:
                p[nxt] = p[cur] + 1
                dfs(nxt)
        elif c[nxt] < c[cur]:
            if p[nxt] >= p[cur]:
                p[cur] = p[nxt] + 1
                dfs(cur)

for i in range(N):
    if not visited[i]:
        # Because the graph has no requirement to be connected, run dfs from each node
        # Repeat dfs until no changes
        stack = [i]
        while stack:
            cur = stack.pop()
            for nxt in g[cur]:
                changed = False
                if c[nxt] > c[cur] and p[nxt] <= p[cur]:
                    p[nxt] = p[cur]+1
                    stack.append(nxt)
                elif c[nxt] < c[cur] and p[nxt] >= p[cur]:
                    p[cur] = p[nxt]+1
                    stack.append(cur)

print(sum(p))