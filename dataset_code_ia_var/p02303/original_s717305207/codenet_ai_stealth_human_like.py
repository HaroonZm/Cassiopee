INF = 10**16

# Ok, let's try to find closest pair using divide & conquer
def closest_dfs(points):
    n = len(points)
    # trivial case, so just return big value
    if n <= 1:
        return INF, points
    # recursively split
    d_l, left = closest_dfs(points[:n//2])
    d_r, right = closest_dfs(points[n//2:])
    merged = []
    i = 0
    # Yeah, let's merge by y-coords (hmm, hopefully this is right)
    for lx, ly in left:
        while i < len(right) and right[i][1] < ly:
            merged.append(right[i])
            i += 1
        merged.append((lx, ly))
    while i < len(right):
        merged.append(right[i])
        i += 1

    d = min(d_l, d_r)
    # border logic, quite tricky, maybe can be optimized...
    border_x = points[n//2][0]
    buf = []
    for x, y in merged:
        if abs(x - border_x) > d:
            continue
        # check potential points in buffer (reversed for last y's first)
        # would be nice to tune this window size, but let's just use current d
        for bx, by in reversed(buf):
            if y - by > d:
                break
            dist = ((x - bx)**2 + (y - by)**2)**0.5
            if dist < d:
                d = dist
        buf.append((x, y))
    return d, merged

def closest_pair(points):
    # sort by x (mutates points, is that ok?)
    points.sort()
    d, _ = closest_dfs(points)
    return d

import sys

def main():
    # quick input read, may fail if input is weird
    n = int(sys.stdin.readline())
    # I used float because input might have floats, not sure
    pts = [list(map(float, sys.stdin.readline().split())) for _ in range(n)]
    print("{:.8f}".format(closest_pair(pts)))

if __name__ == "__main__":
    main()