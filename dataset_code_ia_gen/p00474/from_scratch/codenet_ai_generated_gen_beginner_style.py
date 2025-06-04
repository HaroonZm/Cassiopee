N, L = map(int, input().split())
a = [int(input()) for _ in range(N)]

time = 0
while True:
    # つららが伸びるかどうか判定
    grow = [False]*N
    for i in range(N):
        if a[i] == 0:
            continue
        if i == 0:
            if a[i] > a[i+1]:
                grow[i] = True
        elif i == N-1:
            if a[i] > a[i-1]:
                grow[i] = True
        else:
            if a[i] > a[i-1] and a[i] > a[i+1]:
                grow[i] = True

    # 伸びるつららがなければ終わり
    if not any(grow):
        break

    time += 1

    # つららを伸ばす
    for i in range(N):
        if grow[i]:
            a[i] += 1

    # つららが折れる判定
    for i in range(N):
        if a[i] >= L:
            a[i] = 0

# すべて折れるまでの時間を出力
print(time)