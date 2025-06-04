import sys

for line in sys.stdin:
    x,y = map(int,line.split())
    if x == 0 and y == 0:
        break
    seen = {}
    remainder = x % y
    pos = 0
    while remainder != 0 and remainder not in seen:
        seen[remainder] = pos
        remainder = (remainder * 10) % y
        pos += 1
    if remainder == 0:
        print(pos, 0)
    else:
        print(seen[remainder], pos - seen[remainder])