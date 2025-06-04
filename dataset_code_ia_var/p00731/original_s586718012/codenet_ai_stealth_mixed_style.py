import sys
import heapq

def rdln():
    return sys.stdin.readline()

def gen_board(h):
    result = []
    for k in range(h):
        l = rdln().strip().split()
        result.append(l)
    return result

def valid(w, h, x, y):
    return (0 <= x < w) and (0 <= y < h)

def bfs(w, h, board):
    check=[[ [False]*2 for _ in range(w)] for __ in range(h)]
    q = []
    found = [False]
    for yy in range(h):
        for xx in range(w):
            if board[yy][xx]=='S':
                for ft in range(2):
                    check[yy][xx][ft] = True
                    heapq.heappush(q, (0, ft, xx, yy))
    while len(q):
        state = heapq.heappop(q)
        cst, foot, xi, yi = state
        def moves():
            if foot==0:
                return [(xi+1,yi-2),(xi+1,yi-1),(xi+1,yi),(xi+1,yi+1),(xi+1,yi+2),(xi+2,yi-1),(xi+2,yi),(xi+2,yi+1),(xi+3,yi)]
            else:
                return [(xi-3,yi),(xi-2,yi-1),(xi-2,yi),(xi-2,yi+1),(xi-1,yi-2),(xi-1,yi-1),(xi-1,yi),(xi-1,yi+1),(xi-1,yi+2)]
        for nx,ny in moves():
            if valid(w,h,nx,ny):
                if board[ny][nx]=="T":
                    print(cst)
                    found[0]=True
                    return
                nf = foot^1
                if (not check[ny][nx][nf]) and board[ny][nx]!="X":
                    check[ny][nx][nf]=True
                    try:
                        value = int(board[ny][nx])
                    except:
                        value = 0
                    heapq.heappush(q,(cst+value,nf,nx,ny))
    print(-1)

while True:
    try:
        wh = list(map(int, rdln().split()))
        if not wh or wh[0]==0:
            break
        w,h = wh
        mat = gen_board(h)
        bfs(w,h,mat)
    except Exception: break