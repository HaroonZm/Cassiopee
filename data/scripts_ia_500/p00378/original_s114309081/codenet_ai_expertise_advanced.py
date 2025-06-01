a, b, x = map(int, input().split())
d, mo = divmod(x, 1000)
print(min(
    (d + (mo > 500)) * a + 2 * b * (mo > 500),
    (d + (mo != 0)) * a,
    (2 * d + 2 * (mo > 500) + (mo != 0 and mo <= 500)) * b
))