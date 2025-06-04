n = int(input())
i, ans = 1, 0
while i * i <= n:
    if n % i == 0:
        num = n // i
        ans = max(ans, len(str(num)), len(str(i)))
    i += 1
print(ans)