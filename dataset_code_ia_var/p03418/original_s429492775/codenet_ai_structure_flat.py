n, k = map(int, open(0).read().split())

ans = 0
b = k + 1
while b <= n:
    c = n // b * (b - k)
    if k != 0:
        d = max(0, n % b - k + 1)
    else:
        d = n % b
    ans += c
    ans += d
    b += 1

print(ans)