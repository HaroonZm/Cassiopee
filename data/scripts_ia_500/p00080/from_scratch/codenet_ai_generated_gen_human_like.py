while True:
    q = int(input())
    if q == -1:
        break
    x = q / 2
    while abs(x**3 - q) >= 0.00001 * q:
        x = x - (x**3 - q) / (3 * x**2)
    print(x)