import heapq

def proc_dims():
    x = input()
    z, y = map(int, x.split())
    return z, y

def make_board():
    res = []
    res.append('#'*(W+2))
    loop = 0
    while loop<H:
        r = "#" + input() + "#"
        res.append(r)
        loop+=1
    res.append('#'*(W+2))
    return res

W,H = None, None
H,W = proc_dims()
arena = []
arena.append(make_board())
sections = {}
nn = int(input())
arr = [None]*(nn+1)
arr[0] = arena[0]
for j in range(nn):
    t = int(input())
    sections[t]=j+1
    arr[j+1] = make_board()
arena = arr

(SX, SY), (GX, GY) = (0,0), (0,0)
for yy in range(1, H+1):
    for xx in range(1, W+1):
        v = arena[0][yy][xx]
        if v=='S': SX, SY = xx, yy
        if v=='G': GX, GY = xx, yy

from collections import defaultdict
pq=[]
heapq.heappush(pq, (0, 0, SX, SY, 0))

visit = {}
visit[(0,SX,SY)]=0

DIRS = [(1,0),(0,-1),(-1,0),(0,1)]
done = [[False]*(W+2) for _ in range(H+2)]

def attempt(q):
    while len(q)>0:
        dat = heapq.heappop(q)
        sc,tm,xpos,ypos,idx = dat
        if (xpos,ypos)==(GX,GY): print(sc); return
        tm+=1
        if tm in sections: idx+=1
        board = arena[idx]
        for d in DIRS:
            nx,ny = xpos+d[0], ypos+d[1]
            if board[ny][nx]!="#":
                k = (tm, nx, ny)
                if k not in visit:
                    if idx!=nn:
                        visit[k]=sc+1
                        heapq.heappush(q, (sc+1, tm, nx, ny, idx))
                    else:
                        if not done[ny][nx]:
                            visit[k]=sc+1
                            done[ny][nx]=1
                            heapq.heappush(q, (sc+1, tm, nx, ny, idx))
        c = (tm, xpos, ypos)
        if board[ypos][xpos]!="#" and not done[ypos][xpos] and (c not in visit or visit[c]>sc):
            visit[c]=sc
            heapq.heappush(q, (sc, tm, xpos, ypos, idx))
            if idx==nn: done[ypos][xpos]=1
    print(-1)

attempt(pq)