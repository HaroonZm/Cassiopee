from bisect import bisect_left
from functools import partial
from operator import itemgetter
from itertools import accumulate

INF = float('inf')

def main():
    w, h = map(int, input().split())
    n = int(input())

    xlst, ylst = zip(*(map(int, input().split()) for _ in range(n)))

    sx = sorted(xlst)
    sy = sorted(ylst)
    cumsumx = tuple(accumulate(sx))
    cumsumy = tuple(accumulate(sy))
    accx = cumsumx[-1]
    accy = cumsumy[-1]

    def get_median_pair(arr):
        mid = n // 2
        if n % 2:
            return (arr[mid], arr[mid])
        else:
            return (arr[mid - 1], arr[mid])

    clx, crx = get_median_pair(sx)
    cly, cry = get_median_pair(sy)

    plx = bisect_left(sx, clx)
    prx = bisect_left(sx, crx)
    ply = bisect_left(sy, cly)
    pry = bisect_left(sy, cry)

    def compute_len(acc, cumsum, idx, c, n_):
        if idx:
            return (acc - 2 * cumsum[idx - 1] - c * (n_ - 2 * idx)) * 2
        else:
            return (acc - c * n_) * 2

    xllen = compute_len(accx, cumsumx, plx, clx, n)
    xrlen = compute_len(accx, cumsumx, prx, crx, n)
    yllen = compute_len(accy, cumsumy, ply, cly, n)
    yrlen = compute_len(accy, cumsumy, pry, cry, n)

    ans = INF
    ansx = ansy = 0
    max_sumd = -1

    median_xs = (clx, crx)
    median_ys = (cly, cry)
    len_xs = (xllen, xrlen)
    len_ys = (yllen, yrlen)

    for xi, yi in zip(xlst, ylst):
        medx_idx = 1 if xi <= clx else 0
        medy_idx = 1 if yi <= cly else 0
        cx = median_xs[medx_idx]
        cy = median_ys[medy_idx]
        xlen = len_xs[medx_idx]
        ylen = len_ys[medy_idx]

        dx = abs(xi - cx)
        dy = abs(yi - cy)
        sumd = dx + dy

        if sumd < max_sumd:
            continue
        if sumd > max_sumd:
            max_sumd = sumd

        tlen = xlen + ylen - max_sumd
        candidate = (tlen, cx, cy)
        if candidate < (ans, ansx, ansy):
            ans, ansx, ansy = candidate

    print(ans)
    print(ansx, ansy)

main()