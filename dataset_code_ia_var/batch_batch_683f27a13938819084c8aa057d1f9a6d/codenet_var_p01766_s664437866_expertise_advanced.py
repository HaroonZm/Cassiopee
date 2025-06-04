import sys
from math import hypot
from functools import partial

def fmt(x):
    return f"{x:.10f}"

def main():
    n = int(sys.stdin.readline())
    last = [-1]*5
    result = {0: (-1, -1), 1: (-1, -1)}  # {type: (max_dist, time)}

    for _ in range(n):
        l = list(map(int, sys.stdin.readline().split()))
        cond1 = last[2] != l[2]
        cond2 = last[1] == -1 or last[1] == l[1]
        if cond1 or cond2:
            last = l
            continue

        if last[1] != l[1]:
            d = hypot(last[3] - l[3], last[4] - l[4])
            t_diff = l[0] - last[0]
            typ = l[2]
            maxd, t = result[typ]
            if maxd <= d:
                result[typ] = (d, t_diff)
        last = l

    for typ in (0, 1):
        dist, t = result[typ]
        if dist != -1:
            print(f"{fmt(round(dist, 10))} {fmt(t/60)}")
        else:
            print("-1 -1")

if __name__ == "__main__":
    main()