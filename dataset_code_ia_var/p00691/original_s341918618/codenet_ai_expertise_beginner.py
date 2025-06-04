a = 1 / 3
while True:
    z = int(input())
    if z == 0:
        break
    m = 0
    zz = z * z * z
    max_x = int(z / (2 ** a)) + 1
    for x in range(1, max_x):
        xx = x * x * x
        y = int((zz - xx) ** a)
        yy = y * y * y
        if m < yy + xx:
            m = yy + xx
    print(zz - m)