from bisect import bisect
n, a, b, q = map(int, input().split())
W = [input().split() for _ in range(a)]
X = []
C = []
for w in W:
    X.append(int(w[0]))
    C.append(w[1])
P = []
Y = []
for _ in range(b):
    p = list(map(int, input().split()))
    P.append(p)
    Y.append(p[0])
Y.append(n+1)
D = []
for i in range(b):
    y0 = P[i][0]
    h = P[i][1]
    y1 = Y[i+1]
    l = y1 - y0
    D.append(min(y0 - h, l))
idx = 0
S = {}
for i in range(a):
    x = X[i]
    c = C[i]
    S[x] = c
    if x < Y[0]:
        continue
    while Y[idx+1] <= x:
        idx += 1
    ii = idx
    jj = ii
    z = x
    while Y[0] <= z:
        while z < Y[ii]:
            ii -= 1
        y0 = P[ii][0]
        h = P[ii][1]
        y1 = Y[ii+1]
        if h == 0:
            break
        z = h + ((z - y0) % D[ii])
        assert z < y0
        S[z] = c
Z = []
for _ in range(q):
    Z.append(int(input()))
res = []
for query_z in Z:
    z = query_z
    flag = False
    if z in S:
        res.append(S[z])
        continue
    i = bisect(Y, z) - 1
    while Y[0] <= z:
        while z < Y[i]:
            i -= 1
        y0 = P[i][0]
        h = P[i][1]
        y1 = Y[i+1]
        if h == 0:
            break
        z = h + ((z - y0) % D[i])
        assert z < y0
        if z in S:
            res.append(S[z])
            flag = True
            break
    if not flag:
        res.append('?')
print(''.join(res))