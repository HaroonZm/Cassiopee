import math
while True:
    q = int(input())
    if q == -1:
        break
    x = q / 2
    while True:
        if math.fabs((x ** 3) - q) < 0.00001 * q:
            break
        x = x - ((x ** 3) - q) / (3 * (x ** 2))
    print(f"{x:.6f}")