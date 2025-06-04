a, b = map(int, input().split())
print(max((a << 1) - 1, (b << 1) - 1, a + b))