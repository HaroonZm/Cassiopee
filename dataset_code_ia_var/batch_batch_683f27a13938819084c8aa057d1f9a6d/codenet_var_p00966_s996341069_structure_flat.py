from bisect import bisect
n, a, b, q = map(int, input().split())
W = [input().split() for _ in range(a)]
X = [int(w[0]) for w in W]
C = [w[1] for w in W]
P = [list(map(int, input().split())) for _ in range(b)]
Y = [p[0] for p in P] + [n+1]
D = [0]*b
for i in range(b):
    y0, h = P[i][0], P[i][1]
    y1 = Y[i+1]
    D[i] = min(y0 - h, y1 - y0)
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
    j = idx
    while Y[0] <= x:
        while x < Y[j]:
            j -= 1
        y0 = P[j][0]
        h = P[j][1]
        if h == 0:
            break
        x = h + ((x - y0) % D[j])
        S[x] = c
Z = [int(input()) for _ in range(q)]
res = []
for query in Z:
    z = query
    found = False
    if z in S:
        res.append(S[z])
        continue
    i = bisect(Y, z)-1
    while Y[0] <= z:
        while z < Y[i]:
            i -= 1
        y0 = P[i][0]
        h = P[i][1]
        if h == 0:
            break
        z = h + ((z - y0) % D[i])
        if z in S:
            res.append(S[z])
            found = True
            break
    if not found:
        res.append('?')
print(''.join(res))