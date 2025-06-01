from sys import stdin
for line in stdin:
    a = list(map(int, line.strip()))
    if not a:
        break
    for i in range(9, 0, -1):
        a[:i] = [(x + y) % 10 for x, y in zip(a, a[1:])]
    print(a[0])