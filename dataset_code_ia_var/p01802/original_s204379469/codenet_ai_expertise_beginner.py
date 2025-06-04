import math

while True:
    values = input().split()
    d = int(values[0])
    e = int(values[1])
    if d == 0 and e == 0:
        break

    sa = d
    if e > d:
        sa = e

    i = 0
    while i <= d // 2:
        a = i
        b = d - i
        c = math.sqrt(a * a + b * b)
        diff = abs(c - e)
        if diff < sa:
            sa = diff
        i = i + 1

    print(sa)