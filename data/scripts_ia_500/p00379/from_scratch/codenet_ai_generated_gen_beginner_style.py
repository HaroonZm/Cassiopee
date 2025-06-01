a, n, m = map(int, input().split())

count = 0
for x in range(1, m+1):
    y = sum(int(d) for d in str(x))
    if (y + a) ** n == x:
        count += 1

print(count)