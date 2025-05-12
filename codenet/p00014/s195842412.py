import sys
for l in sys.stdin:
    d = int(l)
    result = 0
    for x in range(d, 600-d+1, d):
        result += d*x**2
    print(result)