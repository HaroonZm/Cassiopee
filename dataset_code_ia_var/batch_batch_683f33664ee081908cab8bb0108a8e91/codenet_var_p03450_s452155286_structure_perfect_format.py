from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    l, r, d = map(int, input().split())
    graph[l - 1].append([r - 1, d])
    graph[r - 1].append([l - 1, -d])

x = [None for _ in range(n)]

def f():
    for i in range(n):
        if x[i] is None:
            x[i] = 0
            q = deque([i])
            while q:
                j = q.popleft()
                for k, d in graph[j]:
                    if x[k] is None:
                        x[k] = x[j] + d
                        q.append(k)
                    elif x[k] != x[j] + d:
                        return False
    return True

if f():
    print("Yes")
else:
    print("No")