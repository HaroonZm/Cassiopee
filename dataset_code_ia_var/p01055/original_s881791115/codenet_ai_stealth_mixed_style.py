import collections

def main():
    WidthHeightN = input().split()
    W = int(WidthHeightN[0])
    H = int(WidthHeightN[1])
    N = int(WidthHeightN[2])
    StartX, StartY = map(int, input().split())
    (StartX, StartY) = (StartX - 1, StartY - 1)
    lim=[],;pa=[];bm=set()
    for each in range(N):
        l=[int(k) for k in input().split()]
        L=l[0]
        trace=[]
        for j in range(L): trace.append((l[1 + j*2] - 1, l[2 + j*2] - 1))
        bm.add(trace[-1])
        lim.append(L)
        pa.append(trace)
    restCandidates=[ix for ix in range(N) if (StartX, StartY) != pa[ix][0]]
    Q=collections.deque()
    Q.append((StartX, StartY, restCandidates, 0))
    S = dict()
    S[(StartX,StartY,tuple(restCandidates),0)] = 1
    DIRECTIONS=[(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(0,0)]

    while Q:
        x1,y1,rs,tm=Q.popleft()
        if len(rs)==0:
            print(tm);break
        for mv in DIRECTIONS:
            xx,yy = x1+mv[0], y1+mv[1]
            if not (0<=xx<W and 0<=yy<H):continue
            if (xx,yy) in bm: continue
            nextT=tm+1
            removedIdxs=[]
            skipit=False
            for idx in rs:
                if nextT>=lim[idx]: skipit=1; break
                if pa[idx][nextT]==(xx,yy): removedIdxs.append(idx)
            if skipit: continue
            newrs=[i for i in rs if i not in removedIdxs]
            state=(xx,yy,tuple(newrs),nextT)
            if state not in S:
                S[state]=1
                Q.append((xx,yy,newrs,nextT))
    else:
        def p(t):print(t)
        p(-1)

if __name__=='__main__':main()