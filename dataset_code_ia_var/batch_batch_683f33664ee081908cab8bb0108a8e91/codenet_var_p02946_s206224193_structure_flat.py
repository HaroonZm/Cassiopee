k, x = map(int, input().split())
i = x - k + 1
while i < x + k:
    if i >= -1000000 and i <= 1000000:
        print(i, end=' ')
    i += 1