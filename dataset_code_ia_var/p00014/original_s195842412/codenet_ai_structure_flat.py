import sys
for l in sys.stdin:
    d = int(l)
    result = 0
    x = d
    while x <= 600 - d:
        result += d * x * x
        x += d
    print(result)