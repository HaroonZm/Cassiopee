from collections import deque
import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    W, H = map(int, readline().split())
    if W == H == 0:
        return False
    S = [readline().strip() for i in range(H)]
    dd = ((-1, 0), (0, -1), (1, 0), (0, 1))
    sx = sy = gx = gy = 0
    for i in range(H):
        Si = S[i]
        for j in range(W):
            if Si[j] == "K":
                sy = i; sx = j
            elif Si[j] == "M":
                gy = i; gx = j
    ks = kg = 0
    for k in range(4):
        dx, dy = dd[k]
        if S[sy+dy][sx+dx] != "#":
            ks = k
        if S[gy+dy][gx+dx] != "#":
            kg = k
    dx, dy = dd[ks]
    sx1 = sx; sy1 = sy
    while S[sy1+dy][sx1+dx] != "#":
        sx1 += dx; sy1 += dy
    dx, dy = dd[kg]
    gx1 = gx; gy1 = gy
    while S[gy1+dy][gx1+dx] != "#":
        gx1 += dx; gy1 += dy
    N = W*H*4
    G0 = [[[] for i in range(2)] for j in range(N)]
    G1 = [[[] for i in range(2)] for j in range(N)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                continue
            for k in range(4):
                dx, dy = dd[k]
                x = j; y = i
                while S[y+dy][x+dx] != "#":
                    x += dx; y += dy
                dx1, dy1 = dd[k-1]
                if S[i+dy1][j+dx1] == "#":
                    p0 = (i*W + j)*4 + (k-1)%4
                    p1 = (y*W + x)*4 + k
                    G0[p0][1].append(p1)
                    G1[p1][1].append(p0)
                dx2, dy2 = dd[k-3]
                if S[i+dy2][j+dx2] == "#":
                    p0 = (i*W + j)*4 + (k+1)%4
                    p1 = (y*W + x)*4 + k
                    G0[p0][0].append(p1)
                    G1[p1][0].append(p0)
    used = set()
    que = deque()
    for k in range(4):
        if k != ks:
            s = ((sy1*W + sx1)*4 + ks, (sy*W + sx)*4 + k)
            que.append(s)
            used.add(s)
    while que:
        v1, v2 = que.popleft()
        for k in range(2):
            for w1 in G0[v1][k]:
                for w2 in G1[v2][k^1]:
                    s = (w1, w2)
                    if s in used:
                        continue
                    que.append(s)
                    used.add(s)
    ok = 0
    for k in range(4):
        if k != kg:
            s = ((gy*W + gx)*4 + k, (gy1*W + gx1)*4 + kg)
            if s in used:
                ok = 1
    if ok:
        write("He can accomplish his mission.\n")
        return True
    que = deque([(sy1*W + sx1)*4 + ks])
    used = [0]*N
    used[(sy1*W + sx1)*4 + ks] = 1
    while que:
        v = que.popleft()
        for w in G0[v][0]:
            if used[w]:
                continue
            used[w] = 1
            que.append(w)
        for w in G0[v][1]:
            if used[w]:
                continue
            used[w] = 1
            que.append(w)
    for k in range(4):
        if used[(gy*W + gx)*4 + k]:
            ok = 1
    if ok:
        write("He cannot return to the kitchen.\n")
    else:
        write("He cannot bring tea to his master.\n")
    return True
while solve():
    ...