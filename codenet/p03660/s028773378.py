from collections import deque
n = int(input())
g = [[] for i in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

parent = [-1 for i in range(n)]
dist = [-1 for i in range(n)]
flag = [0 for i in range(n)]

def dfs(s):
    flag[s] = 1
    dist[s] = 0
    d = 0
    q = deque([(s, d)])

    while len(q) > 0:
        v = q.popleft()
        for i in g[v[0]]:
            if flag[i]:
                continue
            flag[i] = 1
            parent[i] = v[0]
            dist[i] = v[1] + 1
            q.append((i, v[1] + 1))

parent2 = [-1 for i in range(n)]
dist2 = [-1 for i in range(n)]
flag2 = [0 for i in range(n)]

def dfs_f(s):
    count2 = 0
    flag2[s] = 1
    dist2[s] = 0
    d = 0
    q = deque([(s, d)])

    while len(q) > 0:
        v = q.popleft()
        for i in g[v[0]]:
            if flag2[i]:
                continue
            count2 += 1
            flag2[i] = 1
            parent2[i] = v
            dist2[i] = v[1] + 1
            q.append((i, v[1] + 1))
    return count2

parent3 = [-1 for i in range(n)]
dist3 = [-1 for i in range(n)]
flag3 = [0 for i in range(n)]

def dfs_s(s):
    count3 = 0
    flag3[s] = 1
    dist3[s] = 0
    d = 0
    q = deque([(s, d)])

    while len(q) > 0:
        v = q.popleft()
        for i in g[v[0]]:
            if flag3[i]:
                continue
            count3 += 1
            flag3[i] = 1
            parent3[i] = v[0]
            dist3[i] = v[1] + 1
            q.append((i, v[1] + 1))
    return count3

dfs(0)
D = dist[n-1]

j = n-1
flag2[n-1] = 1
flag3[0] = 1
for i in range(D):
    if (D - i) >= (D+2)//2:
        flag2[j] = 1
        j = parent[j]
    else:
        flag3[j] = 1
        j = parent[j]

df = dfs_f(0)
ds = dfs_s(n-1)

if df > ds:
    print("Fennec")
else:
    print("Snuke")