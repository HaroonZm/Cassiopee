n = int(input())
a = list(map(int, input().split()))
# 1がマックス連続するところ+1の数が出せるサイコロが必要
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