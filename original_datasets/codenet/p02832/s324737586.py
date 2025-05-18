n = int(input())
A = list(map(int, input().split()))

x = 1
ans = 0
flag = False
for a in A:
    if a == x:
        x += 1
        flag = True
    else:
        ans += 1
if flag:
    print(ans)
else:
    print("-1")