import sys
DBG = not True
DBG2 = not True
n, a, b = map(int, input().split())
MAXM = 18
r = [0] * MAXM
s = [0] * MAXM
r[0] = [0]
r[1] = [0, 1]
s[1] = [0, 1]
p1a = [0, 1, 3, 2]
p2a = [3, 1, 0, 2, 2, 0, 1, 3]

for m in range(3, MAXM, 2):
    s[m] = [0] * (2 ** m)
    for i in range(2 ** (m - 2)):
        hi = s[m - 2][i] << 2
        for j in range(4):
            s[m][4 * i + j] = hi + (p1a[j] if i == 0 else p2a[4 * (i % 2) + j])
            if DBG2:
                print("set s m {} i {} j {} - {}".format(m, i, j, s[m][4 * i + j]))

for m in range(2, MAXM):
    r[m] = [0] * (2 ** m)
    for i in range(2 ** (m - 1)):
        r[m][i] = r[m - 1][i]
        r[m][2 ** m - 1 - i] = 2 ** (m - 1) + r[m - 1][i]

z = a ^ b
cnt = 0
d = []
for i in range(MAXM):
    if z & (1 << i) != 0:
        cnt += 1
        d.append(i)
if cnt % 2 == 0:
    print('NO')
    sys.exit(0)
else:
    print('YES')

sz = len(d)
if DBG:
    print("n {} a {} b {} sz {} d:".format(n, a, b, sz))
    print(d)

for i in range(2 ** sz):
    for j in range(2 ** (n - sz)):
        hi = (s[sz][i] << (n - sz))
        if i % 2 == 0:
            lo = r[n - sz][j]
        else:
            lo = r[n - sz][2 ** (n - sz) - 1 - j]
        z2 = hi + lo

        xpos = n - len(d)
        ypos = 0
        t = 0
        for idx in range(n):
            if DBG2:
                print("sw lp i {} xp {} yp {} t {}".format(idx, xpos, ypos, t))
            if idx in d:
                t += ((z2 >> xpos) & 1) << idx
                xpos += 1
            else:
                t += ((z2 >> ypos) & 1) << idx
                ypos += 1
        sw = t
        if DBG:
            print("i {} j {} hi {} lo {} z2 {} sw {}".format(i, j, hi, lo, z2, sw))
        sys.stdout.write(str(a ^ sw) + ' ')
print('')