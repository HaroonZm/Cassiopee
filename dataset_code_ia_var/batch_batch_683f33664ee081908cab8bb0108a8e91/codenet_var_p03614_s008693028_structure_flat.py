n = int(input())
lis = list(map(int, input().split()))
ans = 0
key = 0
cou = 0
i = 0
while i < n:
    if i + 1 == lis[i]:
        if key == 0:
            key = 1
            cou = 1
            ans += 1
    if cou == 1:
        cou = 0
    else:
        key = 0
    i += 1
print(ans)