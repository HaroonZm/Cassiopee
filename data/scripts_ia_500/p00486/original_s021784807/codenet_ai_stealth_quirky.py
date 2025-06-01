from bisect import bisect_left as bl, bisect_right as br
INF = 10**20
def input_ints():
    return map(int, input().split())
w,h = input_ints()
n = int(input())
X, Y = zip(*[tuple(map(int, input().split())) for _ in range(n)])
xs = list(X)
ys = list(Y)
sorted_x = sorted(xs)
sorted_xd = sorted(xs*2)
sorted_y = sorted(ys)
sorted_yd = sorted(ys*2)

cum_x = [0]
cum_y = [0]
for i,v in enumerate(sorted_x):
    cum_x.append(cum_x[-1]+v)
for i,v in enumerate(sorted_y):
    cum_y.append(cum_y[-1]+v)

clx = sorted_xd[n-1]
crx = sorted_xd[n]
cly = sorted_yd[n-1]
cry = sorted_yd[n]

ans = INF
ansx = 10**10
ansy = 10**10

for i,(xi,yi) in enumerate(zip(xs,ys)):
    cx = crx if xi <= clx else clx
    cy = cry if yi <= cly else cly

    px = bl(sorted_x, cx)
    py = bl(sorted_y, cy)

    if px>0:
        xlen = (cx*px - cum_x[px]) * 2 + (cum_x[-1] - cum_x[px] - cx*(n - px)) * 2 - abs(xi - cx)
    else:
        xlen = (cum_x[-1] - cx*n)*2 - abs(xi-cx)
    if py>0:
        ylen = (cy*py - cum_y[py]) * 2 + (cum_y[-1] - cum_y[py] - cy*(n - py)) * 2 - abs(yi - cy)
    else:
        ylen = (cum_y[-1] - cy*n)*2 - abs(yi-cy)

    tlen = xlen + ylen
    if ans > tlen or (ans == tlen and (ansx > cx or (ansx == cx and ansy > cy))):
        ans = tlen
        ansx = cx
        ansy = cy

print(ans)
print(ansx, ansy)