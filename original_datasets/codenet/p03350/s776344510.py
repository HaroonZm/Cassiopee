N, K = map(int, input().split())
D = N + 1

d = [[0] * (1 << N) for _ in range(D)]
f = [[0] * (1 << N) for _ in range(D)]

for i in range(D):
    for j, c in enumerate(input()):
        if c == '1':
            d[i][j] = 1

for i in range(1, D):
    for j in range(1 << i):
        t = (j >> (i - 1)) & 1
        r = 0
        while r < i and ((j >> (i - 1 - r)) & 1) == t:
            r += 1
        f[i][j] = r

for i in range(D):
    for ii in range(i + 1, D):
        z = ii - i
        mask = (1 << z) - 1
        for j in range(1 << ii):
            d[i][j >> z] += d[ii][j]
            r = f[z][j & mask]
            if r != z:
                d[ii - r][((j >> z) << (z - r)) | (j & ((1 << (z - r)) - 1))] += d[ii][j]
    for j in range(1 << i):
        if d[i][j] >= K:
            I = i
            J = j
            break

print('' if I == J == 0 else bin(J)[2:].zfill(I))