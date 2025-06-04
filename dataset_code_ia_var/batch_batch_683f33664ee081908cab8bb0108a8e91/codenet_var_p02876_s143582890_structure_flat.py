import sys
input = sys.stdin.readline

N = int(input())
S = 0
Y = []
i = 0
while i < N:
    a, b = map(int, input().split())
    if b > a:
        S += b - a
        Y.append((b, b))
    else:
        Y.append((a, b))
    i += 1

Y.sort()
YY = [0] * (N + 1)
i = 0
while i < N:
    YY[i + 1] = YY[i] + Y[i][0]
    i += 1

ma1 = 0
ma2 = 1
i = 0
while i < N:
    l = 0
    r = N
    while r - l > 1:
        m = (l + r) // 2
        if S - Y[i][0] + Y[i][1] - (YY[m] if m <= i else YY[m + 1] - Y[i][0]) >= 0:
            l = m
        else:
            r = m
    fi = S - Y[i][0] + Y[i][1] - (YY[l] if l <= i else YY[l + 1] - Y[i][0])
    a = l * Y[i][1] + min(fi, Y[i][1])
    b = N * Y[i][1]
    if a * ma2 > b * ma1:
        ma1 = a
        ma2 = b
    i += 1

a = ma1
b = ma2
while b:
    a, b = b, a % b
g = a
print(ma1 // g, ma2 // g)