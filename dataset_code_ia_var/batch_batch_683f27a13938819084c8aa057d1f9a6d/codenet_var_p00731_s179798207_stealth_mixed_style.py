import Queue as Qk

movements = [(( -1, 0), (-1, 1), (-1, 2), (-1, -1), (-1, -2), (-2, 0), (-2, 1), (-2, -1), (-3, 0)),
             ((1, 0), (1, 1), (1, 2), (1, -1), (1, -2), (2, 0), (2, 1), (2, -1), (3, 0))]

def getdims():
    return map(int, raw_input().split())

def gridinp(h):
    return [raw_input().split() for _ in xrange(h)]

while 1:
    W, H = getdims()
    if W==0 and H==0: break
    LIMIT = 1000
    S = gridinp(H)
    dist = [[[LIMIT]*2 for _ in range(W)] for _ in xrange(H)]
    q = Qk.Queue()
    tarpos = list()
    for row in range(H):
        for col, cell in enumerate(S[row]):
            if cell == "S":
                for f in [0, 1]:
                    q.put((col, row, f))
                    dist[row][col][f]=0
            elif cell == "T": tarpos.append((col, row))

    while not q.empty():
        cx, cy, foot = q.get()
        step = 1-foot
        for dx, dy in movements[step]:
            nx = cx + dx; ny = cy + dy
            try:
                spot = S[ny][nx]
            except:
                continue
            if spot=="X" or spot=="S": continue
            price = dist[cy][cx][foot] if spot=="T" else dist[cy][cx][foot]+int(spot)
            if dist[ny][nx][step]>price:
                dist[ny][nx][step]=price
                q.put((nx, ny, step))

    ans = LIMIT
    for tx,ty in tarpos:
        for f in [0,1]:
            if dist[ty][tx][f]<ans: ans=dist[ty][tx][f]
    if ans==LIMIT: print -1
    else:
        print ans