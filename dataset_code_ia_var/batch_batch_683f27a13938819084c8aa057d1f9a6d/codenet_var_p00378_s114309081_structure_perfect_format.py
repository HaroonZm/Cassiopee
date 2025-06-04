a, b, x = map(int, input().split())
d, mo = divmod(x, 1000)
if mo > 500:
    print(min(d * a + 2 * b, (d + 1) * a, (d * 2 + 2) * b))
elif mo != 0:
    print(min(d * a + b, (d + 1) * a, (d * 2 + 1) * b))
else:
    print(min(d * a, d * 2 * b))