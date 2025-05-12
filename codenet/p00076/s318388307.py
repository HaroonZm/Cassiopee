while True:
    n = int(input())
    if not n+1:
        break
    p = 1 + 0j
    for _ in range(n-1):
        d = p * 1j
        d /= abs(d)
        p += d
    print("{:.2f}\n{:.2f}".format(p.real, p.imag))