a, b, c = map(int, input().split())
d1 = 0
d2 = 0
d3 = 0
if a == 5:
    d1 += 1
if b == 5:
    d1 += 1
if c == 5:
    d1 += 1
if a == 7:
    d2 += 1
if b == 7:
    d2 += 1
if c == 7:
    d2 += 1
if a == 0:
    d3 += 1
if b == 0:
    d3 += 1
if c == 0:
    d3 += 1
if d1 == 2 and d2 == 1:
    print('YES')
else:
    print('NO')