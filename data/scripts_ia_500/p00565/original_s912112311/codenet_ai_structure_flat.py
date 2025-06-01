n = int(input())
a = list(map(int, input().split()))
mx = 0
cnt = 0
for i in a:
    if i == 1:
        cnt += 1
        if mx <= cnt:
            mx = cnt
    else:
        cnt = 0
print(mx+1)