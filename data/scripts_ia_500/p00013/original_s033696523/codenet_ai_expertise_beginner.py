import sys

s = []

for l in sys.stdin:
    n = int(l)
    if n == 0:
        print(s.pop())
    else:
        s.append(n)