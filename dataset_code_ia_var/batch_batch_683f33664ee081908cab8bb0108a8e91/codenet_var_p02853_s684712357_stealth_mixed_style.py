get = lambda: list(map(int, input().split()))
a, b = get()
res = 0
points = {3: pow(10, 5), 2: 2 * 10 ** 5, 1: 3 * (10 ** 5)}
for value in [a, b]:
    res = res + points.get(value, 0)
if all([a == 1, b == 1]):
    res += int(4e5)
print(res)