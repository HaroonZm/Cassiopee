n, k = map(int, input().split())
count = 0
b = k + 1
while b <= n:
    candidate = (n // b) * (b - k)
    mod = n % b
    if mod >= k:
        add = mod - k + 1
        if k == 0:
            add -= 1
        candidate += add
    count += candidate
    b += 1
print(count)