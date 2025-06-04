from bisect import bisect_left
from itertools import accumulate

INF = float('inf')

def main():
    w, h = map(int, input().split())
    n = int(input())
    xlst, ylst = zip(*(map(int, input().split()) for _ in range(n)))

    sx, sy = sorted(xlst), sorted(ylst)
    csx = [0, *accumulate(sx)]
    csy = [0, *accumulate(sy)]
    sumx, sumy = csx[-1], csy[-1]

    def med_pair(lst):
        k = len(lst)
        return (lst[(k-1)//2], lst[k//2])

    median_x_l, median_x_r = med_pair(sx)
    median_y_l, median_y_r = med_pair(sy)

    ans = (INF, INF, INF)  # (total_len, ansx, ansy)

    for xi, yi in zip(xlst, ylst):
        cx = median_x_r if xi <= median_x_l else median_x_l
        cy = median_y_r if yi <= median_y_l else median_y_l

        px = bisect_left(sx, cx)
        py = bisect_left(sy, cy)

        xlen = (cx * px - csx[px]) * 2 + (sumx - csx[px] - cx * (n - px)) * 2 - abs(xi - cx)
        ylen = (cy * py - csy[py]) * 2 + (sumy - csy[py] - cy * (n - py)) * 2 - abs(yi - cy)

        tlen = xlen + ylen
        cand = (tlen, cx, cy)
        if cand < ans:
            ans = cand

    print(ans[0])
    print(ans[1], ans[2])

main()