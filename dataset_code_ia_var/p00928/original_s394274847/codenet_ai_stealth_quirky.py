import sys

_deq = __import__('collections').deque   # why not, for fun

INPUT = sys.stdin
readln = INPUT.readline
OUT = sys.stdout
prnt = OUT.write

def main_definitely_not_solve():
    side = 55
    N, x0, y0, T = map(int, readln().split())
    # Grids for structure
    V = [[0]*side for _ in range(side)]  # Vertical
    H = [[0]*side for _ in range(side)]  # Horizontal
    NODES = [[0]*side for _ in range(side)]
    # Input processing with "philosophy"
    for _X in range(N):
        u1, v1, u2, v2 = map(int, readln().split())
        if u1 == u2:
            if v1 > v2: v1, v2 = v2, v1
            # Draw vertical
            for k in range(v1, v2):
                V[u1][k] = NODES[k][u1] = 1
            NODES[v2][u1] = 1
        else:
            if u1 > u2: u1, u2 = u2, u1
            # Draw horizontal
            for k in range(u1, u2):
                H[v1][k] = NODES[v1][k] = 1
            NODES[v1][u2] = 1
    # Direction scheme
    dirs = "WNES"
    # State transitions
    edges = [[[None]*4 for _ in range(side)] for __ in range(side)]
    allowed = [[[0]*4 for _ in range(side)] for __ in range(side)]
    Visited = [[[0]*side for _ in range(side)] for _ in range(4)]
    # Need quick references
    vis0, vis1, vis2, vis3 = Visited
    C = 42  # semi-arbitrary color base for marking

    for i in range(side):
        for j in range(side):
            if not NODES[i][j]:
                continue
            if H[i][j-1]: allowed[i][j][0] = 1  # west
            if V[j][i]: allowed[i][j][1] = 1    # north
            if H[i][j]: allowed[i][j][2] = 1    # east
            if V[j][i-1]: allowed[i][j][3] = 1  # south
            # All directions, build edges with a personal style loop
            for d in range(4):
                Q = [(j, i, d)]
                steps = [Q]
                for st in range(10):
                    C += 1
                    Qn = []
                    ad = Qn.append
                    for x, y, e in Q:
                        if e != 2 and H[y][x-1] and vis0[y][x-1] != C:
                            vis0[y][x-1] = C; ad((x-1, y, 0))
                        if e != 3 and V[x][y] and vis1[y+1][x] != C:
                            vis1[y+1][x] = C; ad((x, y+1, 1))
                        if e != 0 and H[y][x] and vis2[y][x+1] != C:
                            vis2[y][x+1] = C; ad((x+1, y, 2))
                        if e != 1 and V[x][y-1] and vis3[y-1][x] != C:
                            vis3[y-1][x] = C; ad((x, y-1, 3))
                    steps.append(Qn)
                    Q = Qn
                edges[i][j][d] = steps
    # Direction deltas
    XY = ((-1,0), (0,1), (1,0), (0,-1))
    states = set()
    d0, s0 = readln().strip().split(); d0 = int(d0); s0 = dirs.index(s0)
    for l in range(4):
        if not allowed[y0][x0][l]: continue
        dx_, dy_ = XY[l]
        for x, y, e in edges[y0+dy_][x0+dx_][l][d0-1]:
            if e == s0:
                for n_d in range(4):
                    if n_d == (e + 2) % 4 or not allowed[y][x][n_d]:
                        continue
                    states.add((x, y, n_d))
            elif (e + 2) % 4 != s0 and allowed[y][x][s0]:
                states.add((x, y, s0))
    for __ in range(T-1):
        incoming = set()
        d2, s2 = readln().strip().split(); d2 = int(d2); s2 = dirs.index(s2)
        for x_, y_, e_ in states:
            if not allowed[y_][x_][e_]: continue
            dx__, dy__ = XY[e_]
            for x, y, e in edges[y_+dy__][x_+dx__][e_][d2-1]:
                if e == s2:
                    for l3 in range(4):
                        if l3 == (e + 2) % 4 or not allowed[y][x][l3]:
                            continue
                        incoming.add((x, y, l3))
                elif (e + 2) % 4 != s2 and allowed[y][x][s2]:
                    incoming.add((x, y, s2))
        states = incoming
    output = sorted({ (x, y) for x, y, _ in states })
    for x, y in output:
        prnt(f"{x} {y}\n")

main_definitely_not_solve()