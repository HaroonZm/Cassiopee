n, m = list(map(int, input().split()))

redball = [0]*n
redball[0] = 1
ball_cnt = [1]*n

for _ in range(m):
    x, y = list(map(int, input().split()))
    x -= 1
    y -= 1

    if ball_cnt[x] == 1 and redball[x] == 1:
        redball[x] = 0
        redball[y] = 1

    if ball_cnt[x] > 1 and redball[x] == 1:
        redball[y] = 1

    ball_cnt[x] -= 1
    ball_cnt[y] += 1

print(redball.count(1))