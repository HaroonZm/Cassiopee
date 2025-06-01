def out_p(bx, by, x0, y0, x1, y1):
    return (x0 - bx) * (y1 - by) - (y0 - by) * (x1 - bx)

def sgn(x):
    return (x > 0) - (x < 0)

from sys import stdin
n, *lines = map(str.strip, stdin.read().split('\n'))
n = int(n)

for line in lines[:n]:
    *coords, xk, yk, xs, ys = map(int, line.split())
    xp, yp = coords[::2], coords[1::2]

    def signs(px, py, x, y):
        return [sgn(out_p(px[i], py[i], px[i - 2], py[i - 2], x, y)) for i in range(3)]

    k_in = len(set(signs(xp, yp, xk, yk))) == 1
    s_in = len(set(signs(xp, yp, xs, ys))) == 1

    print("OK" if k_in ^ s_in else "NG")