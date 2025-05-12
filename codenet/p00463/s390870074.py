while True:
    n,m,h,k = map(int, input().split())
    if n == 0: break
    pts = []
    for _ in range(n):
        pts.append(int(input()))
    bars = []
    for _ in range(m):
        bars.append(list(map(int, input().split())))
    bars.sort(key=lambda x: x[1])

    nos = [i for i in range(n)]
    barspt = []

    for bar in bars:
        b = bar[0]-1
        barspt.append([nos[b],nos[b+1],0,0])
        nos[b],nos[b+1] = nos[b+1],nos[b]

    nos = [i for i in range(n)]
    for barid in range(m-1,-1,-1):
        b0 = bars[barid][0]-1
        b1 = bars[barid][0]
        barspt[barid][2] = pts[nos[b0]]
        barspt[barid][3] = pts[nos[b1]]
        pts[nos[b0]],pts[nos[b1]] = pts[nos[b1]],pts[nos[b0]]

    atari = -1
    minsc = sum(pts[0:k])

    hosei = 0
    for bar in barspt:
        if atari <= bar[0]-1 and bar[0]-1 < atari+k and (bar[1]-1 < atari or atari+k <= bar[1]-1):
            sc = bar[2]-bar[3]
            if sc < hosei: hosei = sc
        if atari <= bar[1]-1 and bar[1]-1 < atari+k and (bar[0]-1 < atari or atari+k <= bar[0]-1):
            sc = bar[3]-bar[2]
            if sc < hosei: hosei = sc
    print(minsc+hosei)