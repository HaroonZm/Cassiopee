while True:
    q = int(input())
    if q == -1:
        break
    x = q / 2.0
    while True:
        f = x**3 - q
        if abs(f) < 0.00001 * q:
            break
        x = x - f / (3 * x**2)
    print(x)