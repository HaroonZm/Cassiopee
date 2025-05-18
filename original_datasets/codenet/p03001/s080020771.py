W, H, x, y = map(int, input().split())

s = "{0:.6f}".format(float(W*H/2))

if x == W / 2 and y == H / 2:
    print(s, 1)
else:
    print(s, 0)