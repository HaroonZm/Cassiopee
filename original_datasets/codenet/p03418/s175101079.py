n, k = map(int, input().split())

count = 0
for b in range(k+1, n+1):
    candidate = (n // b) * (b - k)
    mod = n % b
    if mod >= k:
        add = mod - k + 1
        if k == 0:
            add -= 1
        candidate += add
    count += candidate

print(count)