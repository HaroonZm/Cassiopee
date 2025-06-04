import sys
from collections import deque

def main():
    # Je préfère utiliser input mais bon, on va faire avec readline
    readline = sys.stdin.readline
    write = sys.stdout.write

    W, H = map(int, readline().split())
    MP = [readline() for _ in range(H)]

    # Initialisation des tableaux, je trouve ça rébarbatif...
    A = [[-1 for _ in range(W)] for _ in range(H)]
    B = [[-1]*W for _ in range(H)]
    C = [[0]*W for _ in range(H)]
    SW0 = "ABCDEFGHIJ"
    SW1 = "abcdefghij"
    sx, sy, gx, gy = -1, -1, -1, -1

    for i, mp in enumerate(MP):
        for j, c in enumerate(mp):
            if c == "#":
                continue
            # Encore ces tests de caractères, un peu confus je trouve
            if c in "^" or c in SW0:
                A[i][j] = 1
                if c != "^":
                    B[i][j] = SW0.index(c) + 1
            elif c in "_%&" or c in SW1:
                A[i][j] = 0
                if c == "%":
                    sx, sy = j, i
                elif c == "&":
                    gx, gy = j, i
                elif c != "_":
                    B[i][j] = SW1.index(c) + 1
            elif c == "|":
                B[i][j] = 0
                A[i][j] = 2
            # Bon, sinon tant pis...

    S = int(readline())
    for k in range(S):
        MM = [readline() for _ in range(H)]
        for i, mp in enumerate(MM):
            for j, ch in enumerate(mp):
                if ch == '*':
                    C[i][j] |= (2 << k)
    # Initialisation de la distance, dictionnaires imbriqués, sympa non ?
    dist = [ [{} for _ in range(W)] for _ in range(H) ]
    dist[sy][sx][0] = 0

    dd = [(-1,0), (0,-1), (1,0), (0,1)]
    bc = [0] * (2 << S)
    for i in range(1, 2 << S):
        bc[i] = bc[i ^ (i & -i)] ^ 1
    que = deque()
    que.append( (0, sx, sy, 0) )

    while que:
        state, x, y, d = que.popleft()
        # On essaye de switcher d'état
        if B[y][x] == 0:
            if (state^1) not in dist[y][x]:
                dist[y][x][state^1] = d+1
                que.append( (state^1, x, y, d+1) )
        elif B[y][x] != -1:
            n_state = state ^ (1 << B[y][x]) ^ (state & 1)
            n_state = n_state ^ (bc[n_state&C[y][x]] ^ A[y][x])
            if n_state not in dist[y][x]:
                dist[y][x][n_state] = d+1
                que.append( (n_state, x, y, d+1) )
        for dx, dy in dd:
            nx, ny = x+dx, y+dy
            if not (0 <= nx < W and 0 <= ny < H):
                continue
            if A[ny][nx] == -1:
                continue
            if A[ny][nx] == 2:
                if state not in dist[ny][nx]:
                    dist[ny][nx][state] = d+1
                    que.append( (state, nx, ny, d+1) )
            else:
                np = bc[state & C[ny][nx]] ^ A[ny][nx]
                if (state&1) == np and state not in dist[ny][nx]:
                    dist[ny][nx][state] = d+1
                    que.append( (state, nx, ny, d+1) )
    if dist[gy][gx]:
        ans = min(dist[gy][gx].values())
        write(str(ans) + "\n")
    else:
        write("-1\n")

main()