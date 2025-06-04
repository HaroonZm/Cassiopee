a, n, m = map(int, input().split())

count = 0
for y in range(1, 500):  # 500 is arbitrary upper bound for sum of digits + a
    x = (y + a) ** n
    if x > m:
        break
    s = sum(int(d) for d in str(x))
    if s == y:
        count += 1

print(count)