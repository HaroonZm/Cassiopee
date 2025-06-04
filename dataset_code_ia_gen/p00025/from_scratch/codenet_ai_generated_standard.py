import sys

for line in sys.stdin:
    a = list(map(int, line.split()))
    if len(a) < 4:
        continue
    b = list(map(int, sys.stdin.readline().split()))
    hit = sum(x == y for x, y in zip(a, b))
    blow = len(set(a) & set(b)) - hit
    print(hit, blow)