n = int(raw_input())
print sum([i * (n - i + 1) for i in range(1, n + 1)]) - sum([u * (n - v + 1) for u, v in [sorted(map(int, raw_input().split())) for _ in range(n - 1)]])