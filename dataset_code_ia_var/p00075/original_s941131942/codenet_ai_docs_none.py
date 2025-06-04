import sys
for s in sys.stdin:
    n, w, h = map(float, s.split(","))
    if w / h**2 >= 25.0:
        print(int(n))