from bisect import bisect_left as B
MAX = 10 ** 20

def main():
    W, H = map(int, input().split())
    N = int(input())
    Xs, Ys = [], []
    for _ in range(N):
        x, y = map(int, input().split())
        Xs += [x]
        Ys += [y]

    Sx = sorted(Xs)
    Sy = sorted(Ys)
    cx_accum = [0]*(N+1)
    cy_accum = [0]*(N+1)
    for i in range(N):
        cx_accum[i+1] = cx_accum[i] + Sx[i]
        cy_accum[i+1] = cy_accum[i] + Sy[i]

    if N & 1:
        leftx = rightx = Sx[N//2]
        lefty = righty = Sy[N//2]
    else:
        leftx, rightx = Sx[N//2 -1], Sx[N//2]
        lefty, righty = Sy[N//2 -1], Sy[N//2]

    best_total = MAX
    best_x = MAX
    best_y = MAX
    for i in range(N):
        X_, Y_ = Xs[i], Ys[i]
        cx = rightx if X_ <= leftx else leftx
        cy = righty if Y_ <= lefty else lefty

        px = B(Sx, cx)
        py = B(Sy, cy)

        if px > 0:
            left_sum_x = cx * px - cx_accum[px]
            right_sum_x = cx_accum[N] - cx_accum[px] - cx * (N - px)
            xlen = 2 * (left_sum_x + right_sum_x) - abs(X_ - cx)
        else:
            xlen = 2 * (cx_accum[N] - cx * N) - abs(X_ - cx)

        if py > 0:
            left_sum_y = cy * py - cy_accum[py]
            right_sum_y = cy_accum[N] - cy_accum[py] - cy * (N - py)
            ylen = 2 * (left_sum_y + right_sum_y) - abs(Y_ - cy)
        else:
            ylen = 2 * (cy_accum[N] - cy * N) - abs(Y_ - cy)

        total = xlen + ylen

        if (best_total > total or
            (best_total == total and (best_x > cx or (best_x == cx and best_y > cy)))):
            best_total, best_x, best_y = total, cx, cy

    print(best_total)
    print(best_x, best_y)

main()