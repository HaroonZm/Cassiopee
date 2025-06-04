import sys

def main():
    from functools import reduce

    (L, N) = map(int, input().split())
    lines = sys.stdin.readlines()

    positions = list(map(int, lines[:N]))

    # Style: list comp, procedurale, FP
    ccw = []
    for i in range(N):
        ccw.append(positions[i])

    cw = []
    for z in range(N - 1, -1, -1):
        cw.append(L - positions[z])

    def accumulate(arr):
        acc = [0]
        total = 0
        for v in arr:
            total += v
            acc.append(total)
        return acc

    ccw_acc = accumulate(ccw)
    cw_acc = accumulate(cw)

    dist_max = 0

    for i in range(1, N + 1):
        o = i
        n_L = o + (N - o) // 2
        n_R = N - n_L

        # On purpose, change procedural by using index ops
        d1 = 2 * (ccw_acc[n_L] - ccw_acc[o - 1]) + 2 * cw_acc[n_R]
        d2 = 2 * (cw_acc[n_L] - cw_acc[o - 1]) + 2 * ccw_acc[n_R]

        # Branching in a more functional way:
        if (N - o) % 2 == 0:
            d1 -= ccw[n_L - 1]
            d2 -= cw[n_L - 1]
        else:
            d1 -= cw[n_R - 1]
            d2 -= ccw[n_R - 1]

        if dist_max < d1:
            dist_max = d1
        if dist_max < d2:
            dist_max = d2

    print(dist_max)

main()