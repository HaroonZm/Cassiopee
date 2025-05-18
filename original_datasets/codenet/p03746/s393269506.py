import sys
sys.setrecursionlimit(100005)

N, M = map(int, input().split())

E = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    E[A].append(B)
    E[B].append(A)

visited = [False for _ in range(N)]
ans = []

def dfs(p, one):
    if visited[p]:
        return False
    visited[p] = True
    if not one:
        ans.append(p+1)
    for i in E[p]:
        if dfs(i, one):
            break
    if one:
        ans.append(p+1)
    return True

dfs(0, True)
for i in E[0]:
    if dfs(i, False):
        break
print(len(ans))
for i in ans:
    print(i)