from bisect import bisect_left as bl
INF = 10 ** 20

w, h = map(int, input().split())
n = int(input())

xlst = []
ylst = []

for i in range(n):
    x, y = map(int, input().split())
    xlst.append(x)
    ylst.append(y)

sorted_xlst = sorted(xlst)
sorted_ylst = sorted(ylst)
accx = 0
accy = 0
cum_sum_xlst = []
cum_sum_ylst = []

for i in range(n):
    accx += sorted_xlst[i]
    accy += sorted_ylst[i]
    cum_sum_xlst.append(accx)
    cum_sum_ylst.append(accy)

if n % 2:
    clx = crx = sorted_xlst[n // 2]
    cly = cry = sorted_ylst[n // 2]
else:
    clx = sorted_xlst[n // 2 - 1]
    crx = sorted_xlst[n // 2]
    cly = sorted_ylst[n // 2 - 1]
    cry = sorted_ylst[n // 2]

ans = INF
ansx = INF
ansy = INF

for i in range(n):
    xi = xlst[i]
    yi = ylst[i]

    if xi <= clx:
        cx = crx
    else:
        cx = clx

    if yi <= cly:
        cy = cry
    else:
        cy = cly

    px = bl(sorted_xlst, cx)
    py = bl(sorted_ylst, cy)

    if px:
        csx = cum_sum_xlst[px - 1]
        xlen = (cx * px - csx) * 2 + (accx - csx - cx * (n - px)) * 2 - abs(xi - cx)
    else:
        xlen = (accx - cx * n) * 2 - abs(xi - cx)

    if py:
        csy = cum_sum_ylst[py - 1]
        ylen = (cy * py - csy) * 2 + (accy - csy - cy * (n - py)) * 2 - abs(yi - cy)
    else:
        ylen = (accy - cy * n) * 2 - abs(yi - cy)

    tlen = xlen + ylen

    if ans > tlen:
        ans = tlen
        ansx = cx
        ansy = cy
    elif ans == tlen:
        if ansx > cx:
            ansx = cx
            ansy = cy
        elif ansx == cx:
            if ansy > cy:
                ansy = cy

print(ans)
print(ansx, ansy)