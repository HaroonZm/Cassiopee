from sys import stdin

for line in stdin:
    n, m = map(int, line.split())
    if n == m == 0:
        break
    cars = [0] + [*map(int, stdin.readline().split())] if n else [0]
    if m:
        cars.extend(map(int, stdin.readline().split()))
    max_gap = max(b - a for a, b in zip(cars, sorted(cars[1:])))
    print(max_gap)