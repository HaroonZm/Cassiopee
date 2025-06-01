import sys
def calc_hull(points, direction):
    maxcos0 = {"r": -1.0, "l": 1.0}
    hull = []
    p = points[0]
    hull.append(p)
    idx = 0
    while True:
        maxcos = maxcos0[direction]
        q = None
        for i in range(1, len(points)):
            if points[i][1] < p[1] or points[i] == p:
                continue
            v0, v1 = points[i][0] - p[0], points[i][1] - p[1]
            length = (v0*v0 + v1*v1)**0.5
            c = v0 / length
            if direction == "r" and c >= maxcos:
                maxcos = c
                q = points[i]
            elif direction == "l" and c <= maxcos:
                maxcos = c
                q = points[i]
        p = q
        hull.append(q)
        if q == points[-1]:
            break
    return hull

def main():
    while 1:
        try:
            n = int(input())
        except EOFError:
            break
        if n == 0:
            break
        d = []
        for _ in map(None, range(n)):
            line = input()
            d.append([float(x) for x in line.split(",")])
        d.sort(key=lambda x: x[1])
        hull_r = calc_hull(d, "r")
        hull_l = calc_hull(d, "l")
        count = len(d) - (len(hull_r + hull_l) - 2)
        print(count)

if __name__ == "__main__":
    main()