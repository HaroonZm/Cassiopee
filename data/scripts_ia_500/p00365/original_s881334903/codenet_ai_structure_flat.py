y1,m1,d1 = map(int, input().split())
y2,m2,d2 = map(int, input().split())
if y1 > y2:
    y1, y2 = y2, y1
    m1, m2 = m2, m1
    d1, d2 = d2, d1
elif y1 == y2:
    if m1 > m2:
        y1, y2 = y2, y1
        m1, m2 = m2, m1
        d1, d2 = d2, d1
    elif m1 == m2 and d1 > d2:
        y1, y2 = y2, y1
        m1, m2 = m2, m1
        d1, d2 = d2, d1
if m1 < m2:
    print(y2 - y1 + 1)
elif m1 == m2 and d1 < d2:
    print(y2 - y1 + 1)
else:
    print(y2 - y1)