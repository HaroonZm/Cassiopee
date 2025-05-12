import fractions

while True:
    a, b, c = map(int, input().split())
    if not a:
        break
    d = (b ** 2 - 4 * a * c) ** 0.5
    if isinstance(d, complex) or d - int(d) > 1e-6:
        print('Impossible')
        continue
    num1, num2 = -b + int(d), -b - int(d)
    den = 2 * a
    cmn1, cmn2 = fractions.gcd(num1, den), fractions.gcd(num2, den)
    p, q, r, s = den // cmn1, -num1 // cmn1, den // cmn2, -num2 // cmn2
    if (p, q) < (r, s):
        p, q, r, s = r, s, p, q
    print(p, q, r, s)