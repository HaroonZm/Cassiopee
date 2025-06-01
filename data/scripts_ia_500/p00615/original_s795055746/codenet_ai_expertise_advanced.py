from sys import stdin

for line in stdin:
    n, m = map(int, line.split())
    if n == m == 0:
        break
    data = [0]
    data.extend(map(int, next(stdin).split()) if n else [])
    data.extend(map(int, next(stdin).split()) if m else [])
    print(max(b - a for a, b in zip(sorted(data), sorted(data)[1:])))