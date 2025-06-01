import sys
from sys import stdin
input = lambda: next(iter(stdin.readline, ''))

def complex_closest(pt_list, sz):
    from math import inf as oo, sqrt as rt
    def recursive(arr):
        if len(arr) < 2:
            return oo
        mid = len(arr) >> 1
        xm = arr[mid][0]
        left_min = recursive(arr[:mid])
        right_min = recursive(arr[mid:])
        d = left_min if left_min < right_min else right_min

        arr_y_sorted = list(sorted(arr, key=lambda e: e[1]))
        strip = []
        for p in arr_y_sorted:
            if (p[0]-xm)**2 >= d:
                continue
            i = 0
            while i < len(strip):
                q = strip[i]
                dy = p[1] - q[1]
                if dy*dy >= d:
                    break
                dx = p[0] - q[0]
                dist_sq = dx*dx + dy*dy
                if dist_sq < d:
                    d = dist_sq
                i += 1
            strip.insert(0,p)
        return d
    pts_copy = pt_list[:]
    pts_copy.sort()
    return recursive(pts_copy)

def main(argv):
    n = int(input())
    points = []
    while len(points) < n:
        points += [tuple(map(int,input().split()))]
    res = complex_closest(points, n)
    print(res)

if __name__ == '__main__':
    import sys as _sys
    main(_sys.argv[1:])