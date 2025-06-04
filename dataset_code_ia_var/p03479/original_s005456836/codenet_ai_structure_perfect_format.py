a = list(map(int, input().split()))
ans = 1
n = a[0]
while True:
    n = n * 2
    if n <= a[1]:
        ans = ans + 1
    else:
        break
print(ans)