from sys import stdin

for line in stdin:
    x, y = map(int, line.split())
    if not (x or y):
        break
    print(*sorted((x, y)))