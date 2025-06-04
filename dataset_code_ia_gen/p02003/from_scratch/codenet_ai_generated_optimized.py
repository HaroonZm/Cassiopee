import sys
sys.setrecursionlimit(10**7)

R,C=map(int,input().split())
board=[input() for _ in range(R)]

# Assign ids to holes (cells with '#')
id_map = [[-1]*C for _ in range(R)]
hole_id = 0
for i in range(R):
    for j in range(C):
        if board[i][j] == '#':
            id_map[i][j] = hole_id
            hole_id += 1

# Build bipartite graph from holes
# Left set: holes in black cells (checkerboard)
# Right set: holes in white cells
# Edges: adjacent holes (up/down/left/right)
black_nodes = []
graph = [[] for _ in range(hole_id)]

for i in range(R):
    for j in range(C):
        if id_map[i][j] == -1:
            continue
        u = id_map[i][j]
        if (i+j)%2==0:
            black_nodes.append(u)
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni,nj = i+dx,j+dy
                if 0<=ni<R and 0<=nj<C and id_map[ni][nj]!=-1:
                    v = id_map[ni][nj]
                    graph[u].append(v)

match_to = [-1]*hole_id

def try_match(u,used):
    for v in graph[u]:
        if used[v]:
            continue
        used[v]=True
        if match_to[v]==-1 or try_match(match_to[v],used):
            match_to[v]=u
            return True
    return False

res = 0
for u in black_nodes:
    used = [False]*hole_id
    if try_match(u,used):
        res += 1

# Minimum vertex cover = maximum matching
# Minimum number of tiles needed = number of holes - maximum matching
print(hole_id - res)