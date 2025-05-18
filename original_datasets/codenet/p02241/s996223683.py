n = int(raw_input())
a = []
for i in range(n):
    a.append(map(int, raw_input().split()))
def prim(a):
    color = ['white' for i in range(n)]
    d = [10**9 for i in range(n)]
    p = [-1 for i in range(n)]
    d[0] = 0
    while True:
        mincost = 10**9
        for i in range(n):
            if color[i] != 'black' and d[i] < mincost:
                mincost = d[i]
                u = i
        if mincost == 10**9:
            break
        color[u] = 'black'
        for v in range(n):
            if color[v] != 'black' and a[u][v] != -1:
                if a[u][v] < d[v]:
                    d[v] = a[u][v]
                    p[v] = u
                    color[v] = 'gray'
    print sum(d)
prim(a)