n = int(input())
li = list(map(int, input().split()))
cnt = n - 2
ans = 0
i = 0
while i < cnt:
    a1 = li[i]
    a2 = li[i + 1]
    a3 = li[i + 2]
    if (a1 < a2) & (a2 < a3):
        ans += 1
    if (a3 < a2) & (a2 < a1):
        ans += 1
    i += 1
print(ans)