n, *z = map(int, open(0).read().split())
a, b = [], []
for x, y in zip(*[iter(z)] * 2):
    a += x + y,
    b += x - y,
print(max(abs(max(a) - min(a)), abs(max(b) - min(b))))