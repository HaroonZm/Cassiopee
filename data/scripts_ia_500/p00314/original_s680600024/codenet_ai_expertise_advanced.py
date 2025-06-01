N = int(input())
P = sorted(map(int, input().split()), reverse=True)
result = max((i + 1 for i, p in enumerate(P) if p >= i + 1), default=0)
print(result)