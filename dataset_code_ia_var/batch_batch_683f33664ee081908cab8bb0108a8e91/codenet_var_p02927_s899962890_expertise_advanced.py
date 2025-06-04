from itertools import product

m, d = map(int, input().split())

ans = sum(
    1
    for n in range(10, d + 1)
    if (t := (n // 10) * (n % 10)) <= m and (n % 10) > 1 and (n // 10) > 1 and t != 0
)

print(ans)