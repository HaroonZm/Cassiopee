from sys import stdin

for line in stdin:
    n, m = map(int, line.split())
    if n == 0 and m == 0:
        break
    traffic = []
    if n:
        traffic.extend(map(int, next(stdin).split()))
    if m:
        traffic.extend(map(int, next(stdin).split()))
    traffic.sort()
    max_gap = max((b - a for a, b in zip(traffic, traffic[1:])), default=0)
    print(max_gap)