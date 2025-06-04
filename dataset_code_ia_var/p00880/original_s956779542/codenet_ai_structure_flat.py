from sys import stdin

file_input = stdin

while True:
    line = file_input.readline()
    if not line:
        break
    x1y1x2y2x3y3 = list(map(int, line.split()))
    if len(x1y1x2y2x3y3) < 6:
        continue
    x1, y1, x2, y2, x3, y3 = x1y1x2y2x3y3
    if x1 == y1 == x2 == y2 == 0:
        break
    A = x1 + y1 * 1j
    B = x2 + y2 * 1j
    C = x3 + y3 * 1j
    a = abs(B - C)
    b = abs(C - A)
    c = abs(A - B)
    s = (a + b + c) / 2
    r = (s * (s - a) * (s - b) * (s - c)) ** 0.5 / s
    D = (b * B + c * C) / (c + b)
    BD = abs(D - B)
    I = (BD * A + c * D) / (c + BD)
    d = abs(A - I)
    e = abs(B - I)
    f = abs(C - I)
    r1 = r / 2 / (s - a) * (s + d - r - e - f)
    r2 = r / 2 / (s - b) * (s + e - r - d - f)
    r3 = r / 2 / (s - c) * (s + f - r - d - e)
    print(r1, r2, r3)