import cmath

N = int(input())
XY = []
for _ in range(N):
    x, y = map(int, input().split())
    XY.append(x + y * 1j)

XY2 = []
for z in XY:
    XY2.append(z)
ph = []
for z in XY2:
    ph.append(cmath.phase(z))
tmp = []
for i in range(len(XY2)):
    tmp.append((ph[i], XY2[i]))
tmp.sort()
XY3 = []
for p, z in tmp:
    XY3.append(z)

ans = 0
for i in range(N):
    for j in range(N):
        if i <= j:
            s = 0
            k = i
            while k <= j:
                s += XY3[k]
                k += 1
            if abs(s) > ans:
                ans = abs(s)
        else:
            s = 0
            for k in range(0, j+1):
                s += XY3[k]
            for k in range(i, N):
                s += XY3[k]
            if abs(s) > ans:
                ans = abs(s)

print(ans)