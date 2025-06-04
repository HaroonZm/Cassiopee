n,k = map(int, input().split())
ans = 0
i = 1
while i <= n:
    temp1 = i - k
    if temp1 < 0:
        temp1 = 0
    temp2 = n // i
    ans += temp1 * temp2
    temp3 = n % i - k + 1
    if temp3 < 0:
        temp3 = 0
    ans += temp3
    i += 1
if k != 0:
    print(ans)
else:
    print(ans - n)