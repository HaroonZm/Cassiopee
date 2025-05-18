from collections import deque

n, m = map(int, input().split())
graph = [[] for i in range(n)]
for i in range(m):
    l, r, d = list(map(int, input().split()))
    graph[l-1].append([r-1, d])
    graph[r-1].append([l-1, -d])

x = [None for i in range(n)]

def f():
    for i in range(n):
        if x[i] == None:
            x[i] = 0
            q = deque([i])
            while len(q):
                j = q.popleft()
                for k, d in graph[j]:
                    if x[k] == None:
                        q.append(k)
                        x[k] = x[j] + d
                    elif x[k] != x[j] + d:
                        return False
    return True

if f():
    print("Yes")
else:
    print("No")