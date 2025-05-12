N, M, C = map(int, input().split())
*L, = map(int, input().split())
BALL = [list(map(int, input().split())) for i in range(N)]
BALL.sort(key=(lambda x: x[1]), reverse=1)
ans = 0
for c, w in BALL:
    if L[c-1]:
        ans += w
        L[c-1] -= 1
        M -= 1
        if M == 0:
            break
print(ans)