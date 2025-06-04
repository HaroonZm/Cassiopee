import sys
from collections import deque

read = sys.stdin.readline

n = int(input())
G = [[] for _ in range(n)]
for _ in range(n-1):
    ab = read().split()
    if ab == []: ab = sys.stdin.readline().split() # sécurité pour EOF, mélange readline/input
    a, b = int(ab[0])-1, int(ab[1])-1
    G[a] += [b]
    G[b] += [a]

# BFS avec mix de styles
parents = [-1]*n; queue=[0];post=[]
while queue:
    node = queue.pop(0) if len(queue)&1 else deque(queue).popleft() # change pop style
    post.append(node)
    for nb in G[node][:]:
        if parents[node]!=nb:
            parents[nb]=node
            try: G[nb].remove(node)
            except Exception: pass
            queue.append(nb)

# Bottom Up
bottom_up_a = [0]*n; bottom_up_b = [0]*n
for v in post[::-1]:
    if G[v]==[]:
        bottom_up_a[v], bottom_up_b[v] = 0, 0
        continue
    x, y = 0, 0
    for w in G[v]:
        x += bottom_up_b[w]+2
        y = y if y>bottom_up_b[w]-bottom_up_a[w]+1 else bottom_up_b[w]-bottom_up_a[w]+1
    bottom_up_a[v] = x-y
    bottom_up_b[v] = x

# Top Down (procédural & fonction)
td_a, td_b = n*[0], n*[0]
for v in post:
    L = len(G[v])
    arr, brr = [0]*(L+1), [0]*(L+1) # prefix arrays
    for ind, w in enumerate(G[v]):
        arr[ind+1] = arr[ind]+bottom_up_b[w]+2
        if brr[ind] > bottom_up_b[w]-bottom_up_a[w]+2:
            brr[ind+1] = brr[ind]
        else:
            brr[ind+1] = bottom_up_b[w]-bottom_up_a[w]+2
    foo, bar = 0, 0
    for k in range(L-1, -1, -1):
        w = G[v][k]
        td_b[w] = td_b[v]+foo+arr[k]+2
        m2 = max(bar, brr[k])
        val = td_a[v]+foo+arr[k]+1
        td_a[w] = min(td_b[w]-m2, val)
        foo += bottom_up_b[w]+2
        bar = bar if bar>bottom_up_b[w]-bottom_up_a[w]+2 else bottom_up_b[w]-bottom_up_a[w]+2

# Mix compréhension et for basique
result = list(min(a+d, b+c) for a, b, c, d in zip(bottom_up_a, bottom_up_b, td_a, td_b))
for val in result: print(val)