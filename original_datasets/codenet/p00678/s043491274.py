from math import sqrt

while True:
        n = int(raw_input())

        if n == 0:
                break

        x = [0 for i in range(n)]
        y = [0 for i in range(n)]
        v = [0 for i in range(n)]

        for i in range(n):
                (x[i], y[i], v[i]) = map(int, raw_input().split())

        px = 0.0
        py = 0.0
        d  = 1000.0

        def dist(x1, y1, x2, y2):
                return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

        ans = 100000
        while d > 0.1 ** 8:
                mx = (0, 0)
                for i in range(n):
                        mx = max(mx, (dist(px, py, x[i], y[i]) / v[i], i))

                ans = mx[0]
                px += d / ans * (x[mx[1]] - px)
                py += d / ans * (y[mx[1]] - py)
                d /= 1.01

        print "%.8f" % ans