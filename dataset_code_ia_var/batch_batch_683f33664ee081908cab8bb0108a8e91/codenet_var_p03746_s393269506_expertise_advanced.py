import sys
from functools import partial

sys.setrecursionlimit(100_005)

N, M = map(int, sys.stdin.readline().split())
E = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    E[A-1].append(B-1)
    E[B-1].append(A-1)

visited = [False] * N
ans = []

def dfs(node: int, post: bool) -> bool:
    stack = [(node, post, False)]
    while stack:
        p, one, entered = stack.pop()
        if entered:
            if one:
                ans.append(p+1)
            return True
        if visited[p]:
            continue
        visited[p] = True
        if not one:
            ans.append(p+1)
        stack.append((p, one, True))
        for n in E[p]:
            if not visited[n]:
                stack.append((n, one, False))
                if one:
                    break
    return False

dfs(0, True)
for i in E[0]:
    if dfs(i, False):
        break

print(len(ans))
print('\n'.join(map(str, ans)))