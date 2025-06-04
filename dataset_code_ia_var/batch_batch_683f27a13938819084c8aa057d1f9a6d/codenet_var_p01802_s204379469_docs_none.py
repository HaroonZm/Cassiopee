import math
while True:
    d,e = map(int,input().split())
    sa = max(d,e)
    if d == 0 and e == 0:
        break
    for i in range(math.floor(d/2) + 1):
        if abs(math.sqrt(i ** 2 + (d - i) ** 2) - e) < sa:
            sa = abs(math.sqrt(i ** 2 + (d - i) ** 2) - e)
    print(sa)