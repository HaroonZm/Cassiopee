import heapq
INF_VAR = float("1e12")

def bfs_Alt(L, u, Q, W, H):
    ret, Y, X = heapq.heappop(Q)
    for dy, dx in ((-1,0),(1,0),(0,-1),(0,1)):
        yy, xx = Y+dy, X+dx
        if 0<=yy<H and 0<=xx<W and not u[yy][xx]:
            heapq.heappush(Q, (L[yy][xx], yy, xx))
            u[yy][xx]=True
    return ret

def dic_func(matrix, col, row, sx, sy):
    q = []
    heapq.heappush(q, (1, sy, sx))
    vis = [[False]*col for _ in range(row)]
    vis[sy][sx] = True
    L = [[0,0]]
    mx = 0; count=0
    add = L.append
    while len(q):
        v = bfs_Alt(matrix, vis, q, col, row)
        count += 1
        if mx<v:
            add([v,count])
            mx=v
        else: L[-1][1] += 1
    return L

def resolve():
    get = input
    while 1:
        r = int(get())
        if r==0: break
        d1 = tuple(map(int,get().split()))
        ls1 = []
        for _ in range(d1[1]): ls1.append(list(map(int,get().split())))
        d2 = tuple(map(int,get().split()))
        ls2 = [list(map(int,get().split())) for _ in range(d2[1])]
        a = dic_func(ls1,d1[0],d1[1],d1[2]-1,d1[3]-1)
        b = dic_func(ls2,d2[0],d2[1],d2[2]-1,d2[3]-1)
        x, y, ix, iy, answer = len(a), len(b), 0, len(b)-1, INF_VAR
        while ix<x and iy>0:
            rr1, s1 = a[ix][0], a[ix][1]
            rr2, s2 = b[iy][0], b[iy][1]
            if (s1+s2)<r: ix+=1; continue
            while iy>0 and (s1+s2)>=r:
                iy-=1
                rr2, s2 = b[iy][0], b[iy][1]
            if iy==0 and (s1+s2)>=r:
                sm = rr1+rr2
                if sm<answer: answer=sm
                break
            else:
                if iy<y-1: iy+=1
                rr2 = b[iy][0]
                sm = rr1+rr2
                if sm<answer: answer=sm
            ix+=1
        print(answer)
resolve()