n = int(input())
ans = 1
while (ans * (ans + 1)) // 2 < n:
    ans = ans + 1
print(ans)