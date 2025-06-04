a, b, c = map(int, input().split())
x = a * b * c
if x % 2 == 0:
    print(0)
else:
    m1 = a * b
    m2 = b * c
    m3 = c * a
    if m1 <= m2 and m1 <= m3:
        print(m1)
    elif m2 <= m1 and m2 <= m3:
        print(m2)
    else:
        print(m3)