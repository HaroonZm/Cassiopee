while True:
    z = int(input())
    if z == 0:
        break
    z_cube = z ** 3
    max_sum = 0
    for x in range(1, z):
        for y in range(1, z):
            s = x**3 + y**3
            if s <= z_cube and s > max_sum:
                max_sum = s
    print(z_cube - max_sum)