a, b, c = map(int, input().split())
print((d := c - a) if 0 < d <= b else 0 if d <= 0 else "NA")