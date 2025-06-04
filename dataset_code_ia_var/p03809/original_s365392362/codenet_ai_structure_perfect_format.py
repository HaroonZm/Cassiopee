import sys
sys.setrecursionlimit(500000)
N = int(input())
A = [0] + list(map(int, input().split()))
E = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    E[a].append(b)
    E[b].append(a)

def dfs(v, p=0):
    a = A[v]
    b = []
    for u in E[v]:
        if u != p:
            b.append(dfs(u, v))
    if len(b) == 0:
        return a
    sum_b = sum(b)
    max_b = max(b)
    if a < max_b or 2 * a < sum_b or a > sum_b:
        print("NO")
        exit()
    return 2 * a - sum_b

v = 1
ans = dfs(v)
if (ans == 0 and len(E[v]) > 1) or (ans == A[v] and len(E[v]) == 1):
    print("YES")
else:
    print("NO")