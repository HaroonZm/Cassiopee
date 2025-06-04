from heapq import heappush, heappop
H, W, T, Q = map(int, input().split())
que = []
state = [[0]*(W+1) for _ in range(H+1)]
data1 = [[0]*(W+1) for _ in range(H+1)]
data2 = [[0]*(W+1) for _ in range(H+1)]
for q in range(Q):
    tcs = list(map(int, input().split()))
    t = tcs[0]
    c = tcs[1]
    ps = tcs[2:]
    while que and que[0][0] <= t:
        _, h0, w0 = heappop(que)
        # add(data1, h0, w0, -1)
        h = h0
        while h <= H:
            w0_ = w0
            el = data1[h]
            while w0_ <= W:
                el[w0_] += -1
                w0_ += w0_ & -w0_
            h += h & -h
        # add(data2, h0, w0, 1)
        h = h0
        while h <= H:
            w0_ = w0
            el = data2[h]
            while w0_ <= W:
                el[w0_] += 1
                w0_ += w0_ & -w0_
            h += h & -h
        state[h0][w0] = 2
    if c == 0:
        h0, w0 = ps
        state[h0][w0] = 1
        # add(data1, h0, w0, 1)
        h = h0
        while h <= H:
            w0_ = w0
            el = data1[h]
            while w0_ <= W:
                el[w0_] += 1
                w0_ += w0_ & -w0_
            h += h & -h
        heappush(que, (t + T, h0, w0))
    elif c == 1:
        h0, w0 = ps
        if state[h0][w0] == 2:
            # add(data2, h0, w0, -1)
            h = h0
            while h <= H:
                w0_ = w0
                el = data2[h]
                while w0_ <= W:
                    el[w0_] += -1
                    w0_ += w0_ & -w0_
                h += h & -h
            state[h0][w0] = 0
    else:
        h0, w0, h1, w1 = ps
        # get(data1, h1, w1)
        s = 0
        hh = h1
        while hh:
            ww = w1
            el = data1[hh]
            while ww:
                s += el[ww]
                ww -= ww & -ww
            hh -= hh & -hh
        g11 = s
        # get(data1, h1, w0-1)
        s = 0
        hh = h1
        wv = w0-1
        while hh:
            ww = wv
            el = data1[hh]
            while ww:
                s += el[ww]
                ww -= ww & -ww
            hh -= hh & -hh
        g12 = s
        # get(data1, h0-1, w1)
        s = 0
        hh = h0-1
        wv = w1
        while hh:
            ww = wv
            el = data1[hh]
            while ww:
                s += el[ww]
                ww -= ww & -ww
            hh -= hh & -hh
        g13 = s
        # get(data1, h0-1, w0-1)
        s = 0
        hh = h0-1
        wv = w0-1
        while hh:
            ww = wv
            el = data1[hh]
            while ww:
                s += el[ww]
                ww -= ww & -ww
            hh -= hh & -hh
        g14 = s
        result1 = g11 - g12 - g13 + g14

        # data2
        s = 0
        hh = h1
        wv = w1
        while hh:
            ww = wv
            el = data2[hh]
            while ww:
                s += el[ww]
                ww -= ww & -ww
            hh -= hh & -hh
        g21 = s
        s = 0
        hh = h1
        wv = w0-1
        while hh:
            ww = wv
            el = data2[hh]
            while ww:
                s += el[ww]
                ww -= ww & -ww
            hh -= hh & -hh
        g22 = s
        s = 0
        hh = h0-1
        wv = w1
        while hh:
            ww = wv
            el = data2[hh]
            while ww:
                s += el[ww]
                ww -= ww & -ww
            hh -= hh & -hh
        g23 = s
        s = 0
        hh = h0-1
        wv = w0-1
        while hh:
            ww = wv
            el = data2[hh]
            while ww:
                s += el[ww]
                ww -= ww & -ww
            hh -= hh & -hh
        g24 = s
        result2 = g21 - g22 - g23 + g24
        print(result2, result1)