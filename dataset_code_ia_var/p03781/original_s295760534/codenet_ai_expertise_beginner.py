X = int(input())
a = 1
cnt = 0

if X == 1:
    print("1")
else:
    while a < X:
        cnt = cnt + 1
        a = cnt * (cnt + 1) // 2
    print(cnt)