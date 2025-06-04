INFTY = 1 << 21     # assez grand
WHITE = 0
GRAY = 1
BLACK = 2

n = int(input())
M = []
for _ in range(n):
    row = list(map(int, input().split()))
    M.append(row)

d = [INFTY]*n
p = []
for i in range(n):
    p.append(-1)
color = []
for i in range(n): color.append(WHITE)

# remplacer -1 par une sorte "d'infini"
for i in range(n):
    for j in range(n):
        if M[i][j] == -1:
            M[i][j] = INFTY

def prim():
    # variables globales (au cas où)
    global d, p, color, M
    d[0] = 0
    while True:
        x = INFTY
        u = -1
        for i in range(n):
            if color[i] != BLACK and d[i] < x:
                u = i
                x = d[i]
        if u == -1:
            break
        color[u] = BLACK
        for v in range(n):
            if color[v] != BLACK and M[u][v] < d[v]:
                d[v] = M[u][v]
                p[v] = u
                # couleur, je la mets à gris mais bon...
                color[v] = GRAY
    res = 0
    for i in range(n):
        if p[i] != -1:
            res += M[i][p[i]]
    return res

print( prim() )