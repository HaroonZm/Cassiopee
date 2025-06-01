n, a = int(input()), sorted(map(int, input().split()))
ans = max(
    max((a[-1] + a[-2]) / (a[i + 1] - a[i]) for i in range(n - 2)),
    (a[-1] + a[-4]) / (a[-2] - a[-3]),
    (a[-3] + a[-4]) / (a[-1] - a[-2])
)
print(f"{ans:.8f}")