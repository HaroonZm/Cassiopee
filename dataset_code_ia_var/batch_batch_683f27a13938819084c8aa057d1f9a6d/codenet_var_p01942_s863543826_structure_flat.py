from heapq import heappush, heappop

H,W,T,Q = map(int,input().split())
pint = [[0]*(W+1) for _ in range(H+1)]

bitY = [[0]*(W+1) for _ in range(H+1)]
bitF = [[0]*(W+1) for _ in range(H+1)]

def add(bit, a, b, Z):
    x = a
    while x <= H:
        y = b
        yl = bit[x]
        while y <= W:
            yl[y] += Z
            y += y & -y
        x += x & -x

def s_sum(bit, a, b):
    ret = 0
    x = a
    while x > 0:
        y = b
        yl = bit[x]
        while y > 0:
            ret += yl[y]
            y -= y & -y
        x -= x & -x
    return ret

def ssum(bit,x1,y1,x2,y2):
    return s_sum(bit, x2, y2) - s_sum(bit, x1-1, y2) - s_sum(bit, x2, y1-1) + s_sum(bit, x1-1, y1-1)

q = []
for i in range(Q):
    t,c,*pos = map(int, input().split())
    while q and q[0][0] <= t:
        _,x,y = heappop(q)
        add(bitY, x, y, -1)
        add(bitF, x, y, 1)
        pint[x][y] = 2
    if c == 0:
        h,w = pos
        pint[h][w] = 1
        add(bitY, h, w, 1)
        heappush(q, (t+T, h, w))
    elif c == 1:
        h,w = pos
        if pint[h][w] == 2:
            add(bitF, h, w, -1)
            pint[h][w] = 0
    else:
        h1,w1,h2,w2 = pos
        print(ssum(bitF, h1, w1, h2, w2), ssum(bitY, h1, w1, h2, w2))