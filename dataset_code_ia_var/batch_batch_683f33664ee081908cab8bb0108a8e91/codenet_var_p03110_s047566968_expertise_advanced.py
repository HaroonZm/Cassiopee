from functools import reduce

n = int(input())
total = reduce(
    lambda acc, _: (
        acc[0] + (v := input().split(), float(v[0]) if v[1] == 'JPY' else 0)[1],
        acc[1] + (float(v[0]) if v[1] == 'BTC' else 0)
    ),
    range(n),
    (0.0, 0.0)
)
print(total[0] + total[1] * 380000)