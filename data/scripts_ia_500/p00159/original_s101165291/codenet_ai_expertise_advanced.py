from sys import stdin

for line in stdin:
    n = int(line)
    if n == 0:
        break
    ans, min_diff = min(
        ((i, abs(22 - w / ((h / 100) ** 2)))
         for _ in range(n)
         for i, h, w in [map(int, stdin.readline().split())]),
        key=lambda x: x[1]
    )
    print(ans)