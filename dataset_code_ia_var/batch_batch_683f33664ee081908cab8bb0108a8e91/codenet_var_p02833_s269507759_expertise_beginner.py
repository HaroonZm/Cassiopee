n = int(input())
ans = 0
if n == 0:
    ans = 0
else:
    if n % 2 == 0:
        pwr = 10
        while pwr <= n:
            ans = ans + n // pwr
            pwr = pwr * 5
    else:
        ans = 0
print(ans)