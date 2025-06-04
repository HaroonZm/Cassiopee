r, d = 0, 0
while True:
    try:
        a, b, c = [int(i) for i in raw_input().split(',')]
    except:
        break
    if a == b:
        d += 1
    if a * a + b * b == c * c:
        r += 1
print r
print d