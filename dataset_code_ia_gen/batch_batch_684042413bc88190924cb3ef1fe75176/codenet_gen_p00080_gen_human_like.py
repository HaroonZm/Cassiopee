while True:
    q = input()
    if q == '-1':
        break
    q = int(q)
    x = q / 2
    while True:
        diff = x**3 - q
        if abs(diff) < 0.00001 * q:
            break
        x = x - diff / (3 * x**2)
    print("{:.6f}".format(x))