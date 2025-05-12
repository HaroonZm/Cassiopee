n = int(input())
li_a = list(map(int, input().split()))
ans  = 0
for i in range(n):
    if (i+1) % 2 == 1:
        if li_a[i] % 2 == 1:
            ans += 1
print(ans)