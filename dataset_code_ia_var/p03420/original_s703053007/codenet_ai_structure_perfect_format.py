n, k = map(int, input().split())
count = 0

if k == 0:
    print(n * n)
else:
    for i in range(n):
        if k > i:
            continue
        count = count + (i + 1 - k) * (n // (i + 1))
        mod = n % (i + 1)
        if mod >= k:
            count = count + mod - k + 1
    print(count)