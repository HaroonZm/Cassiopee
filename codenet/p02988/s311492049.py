n = int(input())
li = list(map(int,input().split()))
cnt = n-2
ans = 0
for i in range(cnt):
    a1 = li[i]
    a2 = li[i+1]
    a3 = li[i+2]
    if (a1 < a2) & (a2 < a3):
        ans += 1
    if (a3 < a2) & (a2 < a1):
        ans += 1
print(ans)