n = int(input())
a = list(map(int, input().split()))
ans = 0
i = 0
while i < n:
    if a[i] % 2 == 1:
        ans += 1
    i += 2
print(ans)