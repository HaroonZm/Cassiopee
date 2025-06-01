a, b, c = map(int, input().split())
print(d := c - a if a < c and (d := c - a) <= b else 0 if a >= c else "NA")