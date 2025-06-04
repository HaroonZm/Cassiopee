n = int(input())
k = int(input())
ans = 1
i = 0
while i < n:
    if ans < k:
        ans = ans * 2
    else:
        ans = ans + k
    i = i + 1
print(ans)