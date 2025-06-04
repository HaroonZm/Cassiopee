import sys
sys.setrecursionlimit(10**8)
N = int(input())
G = []
for i in range(N):
    G.append([])
E = []
ans = []
for i in range(N-1):
    ans.append(0)
for i in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append((b-1, i))
    G[b-1].append((a-1, i))
s = input().split()
for i in range(N):
    s[i] = int(s[i])
n = []
for i in range(N):
    n.append(0)
visited = []
for i in range(N):
    visited.append(False)
stack = []
stack.append((0, -1, 0))
while stack:
    x, p, state = stack.pop()
    if state == 0:
        visited[x] = True
        stack.append((x, p, 1))
        for i, e in G[x]:
            if not visited[i]:
                stack.append((i, x, 0))
    else:
        res = 1
        for i, e in G[x]:
            if i != p and visited[i]:
                res += n[i]
                E.append((e, x, i))
        n[x] = res
flag = 0
E.sort()
for i in range(N-1):
    e, a, b = E[i]
    if 2 * n[b] == N:
        flag = e + 1
        continue
    if 2 * n[b] - N == 0:
        ans[e] = 0
    else:
        ans[e] = abs((s[a] - s[b]) // (2 * n[b] - N))
if flag:
    A = s[0]
    for i in range(N-1):
        A -= n[E[i][2]] * ans[i]
    if n[E[flag-1][2]] == 0:
        ans[flag-1] = 0
    else:
        ans[flag-1] = A // n[E[flag-1][2]]
for i in range(N-1):
    print(ans[i])