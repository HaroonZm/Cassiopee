L, N = map(int, input().split())
snake = input()
cnt = 0
for i in range(L-1) :
    if snake[i:i+2] == 'oo' :
        cnt += 1
for i in range(N) :
    L += cnt * 3
    cnt *= 2
print(L)