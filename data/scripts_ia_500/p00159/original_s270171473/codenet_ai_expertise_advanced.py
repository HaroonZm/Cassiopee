from sys import stdin

for line in stdin:
    n = int(line)
    if n == 0:
        break
    ans, minv = None, float('inf')
    for _ in range(n):
        p, h, w = map(int, next(stdin).split())
        bmi = w / (h * 0.01) ** 2
        diff = abs(bmi - 22)
        if diff < minv:
            ans, minv = p, diff
    print(ans)