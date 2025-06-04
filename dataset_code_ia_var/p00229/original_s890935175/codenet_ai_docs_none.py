import sys, math, os, bisect

PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")

while True:
    b, r, g, c, s, t = [int(_) for _ in input().split()]
    if t == 0:
        break
    print(100 + 95 * b + 63 * r + 7 * g + 2 * c - 3 * (t - s))