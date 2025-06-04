import sys

for l in sys.stdin:
    s, w, h = map(float, l.split(","))
    if w / h ** 2 >= 25:
        print(int(s))