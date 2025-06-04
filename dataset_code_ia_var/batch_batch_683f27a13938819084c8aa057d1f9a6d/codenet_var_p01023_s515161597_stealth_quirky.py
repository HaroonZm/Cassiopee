from collections import deque as D

def xXx():
    H, W, N = map(int, input().split())
    M = [list('$' * (W+2))]
    getl = lambda: list('$' + input() + '$')
    [M.append(getl()) for _ in range(H)]
    M.append(list('$' * (W+2)))
    B = [None]*4
    hh = None
    for yy in range(1, H+1):
        for xx in range(1, W+1):
            z = M[yy][xx]
            if z == "S":
                hh = (xx,yy)
                M[yy][xx] = "."
            elif z == "e":
                M[yy][xx] = "."
            elif z in "abcd":
                B[ord(z)-97] = (xx,yy)
                M[yy][xx] = "."
            elif z.isdigit():
                M[yy][xx] = int(z)
    Q = D()
    magic = (hh, tuple(B), 1)
    S = {magic: 0}
    Q.append((0, hh, B, 1))
    dirs = ((-1,0), (0,1), (1,0), (0,-1))
    while Q:
        scr, hd, bd, tgt = Q.popleft()
        if tgt > N:
            print(scr)
            return
        X, Y = hd
        for dlt in dirs:
            nx, ny = X+dlt[0], Y+dlt[1]
            if (nx,ny) in bd: continue
            if M[ny][nx] == "$": continue
            ntgt = tgt
            if M[ny][nx] == tgt: ntgt += 1
            nbd = tuple([hd]+list(bd)[:-1])
            key = ((nx,ny), nbd, ntgt)
            if key not in S:
                S[key] = 1
                Q.append((scr+1, (nx,ny), nbd, ntgt))
    print(-1)

xXx()