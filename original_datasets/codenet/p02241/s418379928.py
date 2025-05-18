INFTY = 1 << 21
WHITE = 0
GRAY = 1
BLACK = 2

n = int(input())
M = [list(map(int, input().split())) for i in range(n)]

d = [INFTY for i in range(n)]
p = [-1 for i in range(n)]
color = [WHITE for i in range(n)]

for i in range(n):
    for j in range(n):
        if (M[i][j] == -1):
            M[i][j] = INFTY

def prim():
    global M, d, p, color
    d[0] = 0
    while(1):
        minv = INFTY
        u = -1
        for i in range(n):
            if (minv > d[i] and color[i] != BLACK):
                u = i
                minv = d[i]
        if (u == -1):
            break
        color[u] = BLACK
        for v in range(n):
            if (color[v] != BLACK and M[u][v] != INFTY):
                if (d[v] > M[u][v]):
                    d[v] = M[u][v]
                    p[v] = u
                    color[v] = GRAY
    
    return sum([M[i][p[i]] for i in range(n) if p[i] != -1])

print(prim())