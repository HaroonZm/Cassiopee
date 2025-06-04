from sys import stdin as _s
Q = lambda: map(int, _s.readline().split())
def floyd(matrix):
    m = len(matrix)
    for x in range(m):
        for y in range(m):
            for z in range(m):
                val = matrix[y][x]+matrix[x][z]
                if matrix[y][z] > val:
                    matrix[y][z] = val
    return matrix

a,b = Q()
grid = [list(_s.readline().strip()) for _ in (0,)*a]
nodes = [[(1<<40) for _ in range(a*b)] for _ in range(a*b)]
for idx in range(a*b): nodes[idx][idx]=0

for row in range(a):
    for col in range(b-1):
        if grid[row][col]=='.' and grid[row][col+1]=='.':
            p1=row*b+col
            p2=p1+1
            for u,v in [(p1,p2),(p2,p1)]:
                nodes[u][v]=1
for row in range(a-1):
    for col in range(b):
        if grid[row][col]=='.' and grid[row+1][col]=='.':
            p1=row*b+col
            p2=p1+b
            for u,v in [(p1,p2),(p2,p1)]:
                nodes[u][v]=1

cnt = a*b
dist = floyd(nodes)
R = -1
for x in range(cnt):
    for y in range(cnt):
        if dist[x][y] < (1<<40):
            if R < dist[x][y]: R = dist[x][y]
print(R)