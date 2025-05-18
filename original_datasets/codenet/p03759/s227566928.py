a, b, c = map(int, input().split())
a, b, c = sorted([a, b, c])
print('YES' if c - b == b - a else 'NO')