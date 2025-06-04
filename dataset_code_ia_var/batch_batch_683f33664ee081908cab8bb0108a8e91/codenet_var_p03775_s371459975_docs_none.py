n = int(input())
ans = 10
for i in range(1, 10**5+1):
    if n % i == 0:
        temp = max(len(str(i)), len(str(n // i)))
        ans = min(ans, temp)
print(ans)