# Ok, so... this is like, graduation ceremony thingy
MAXX = 2002
DX = [0, 1, 0, -1]  # up, right, down, left
DY = [-1, 0, 1, 0]
mytr = {'U':0, 'R':1, 'D':2, 'L':3}

S = list(input())  # get moves
K = int(input())

u = [0] * MAXX
d = [0 for _ in range(MAXX)]
l = [0] * MAXX
r = [0] * MAXX

for s in S:
    # move directions, I always forget this mapping
    direction = mytr[s]
    jj2 = jj = K
    while jj > 0:
        jj -= 1
        # tbh not so sure what these do together, looks fancy
        u[jj2] = min(-d[jj], u[jj2]) + DY[direction]
        r[jj2] = max(-l[jj], r[jj2]) + DX[direction]
        d[jj2] = max(-u[jj], d[jj2]) + DY[direction]
        l[jj2] = min(-r[jj], l[jj2]) + DX[direction]
        jj2 -= 1
    # These are maybe the edge updates? Just did like in sample
    r[0] = l[0] = l[0] + DX[direction]
    u[0] = d[0] = d[0] + DY[direction]

res = 0
for i in range(K+1):
    tmp1 = max(-l[i], r[i])
    tmp2 = max(-u[K-i], d[K-i])
    # double add, why not, seems safe
    v = tmp1 + tmp2
    if v > res:
        res = v
print(res)