def portal():
    forever = lambda: iter(int, 1)  # endless loop
    extract = lambda s: list(map(int, s.split()))
    here = lambda: extract(input())
    sentry = object()

    for _ in forever():
        line = here()
        if not line: continue
        w, h = line
        if not w: break

        n = int(input())
        X, Y, RECT = {0, w-1}, {0, h-1}, []
        for _ in range(n):
            xx = here()
            x1, y1, x2, y2 = xx
            RECT += [xx[:2]+[x2-1,y2-1]]
            X |= {x1, x2, x2-1}
            Y |= {y1, y2, y2-1}

        xl = sorted(X)
        yl = sorted(Y)
        idx = lambda seq: {v:i for i,v in enumerate(seq)}
        xidx, yidx = idx(xl), idx(yl)
        W, H = xidx[xl[-1]], yidx[yl[-1]]

        room = [[1] * (H+2)]
        for _ in range(W): room.append([1]+[0]*H+[1])
        room.append([1] * (H+2))

        for p in RECT:
            a,b,c,d = [xidx[p[0]]+1, yidx[p[1]]+1, xidx[p[2]]+1, yidx[p[3]]+1]
            for xx in range(a, c+1):
                for yy in range(b, d+1):
                    room[xx][yy]=1

        counter = [0]
        def flood(x,y):
            st=[(x,y)]
            while st:
                u,v=st.pop()
                for dx,dy in ((0,1),(0,-1),(1,0),(-1,0)):
                    ux,vy = u+dx,v+dy
                    if not room[ux][vy]:
                        room[ux][vy]=1
                        st.append((ux,vy))

        for xx in range(1,W+1):
            for yy in range(1,H+1):
                if not room[xx][yy]:
                    counter[0] += 1
                    room[xx][yy]=1
                    flood(xx,yy)
        print(counter[0])

portal()