n = int(input())
a = list(map(int, input().split()))
cnt = 0
flag = 0
for i in range(n - 1):
    if flag == 0:
        if a[i] < a[i + 1]:
            flag = 1
        elif a[i] > a[i + 1]:
            flag = -1
    elif flag == 1:
        if a[i] < a[i + 1]:
            flag = 1
        elif a[i] > a[i + 1]:
            flag = 0
            cnt += 1
    elif flag == -1:
        if a[i] > a[i + 1]:
            flag = -1
        if a[i] < a[i + 1]:
            flag = 0
            cnt += 1
print(cnt + 1)