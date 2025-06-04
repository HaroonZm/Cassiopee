L, N = input().split()
L = int(L)
N = int(N)
snake = input()
cnt = 0
for i in range(L - 1):
    if snake[i] == 'o' and snake[i + 1] == 'o':
        cnt = cnt + 1
for i in range(N):
    L = L + (cnt * 3)
    cnt = cnt * 2
print(L)