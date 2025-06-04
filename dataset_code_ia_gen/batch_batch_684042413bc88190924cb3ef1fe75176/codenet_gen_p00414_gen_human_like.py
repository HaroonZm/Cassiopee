L, N = map(int, input().split())
snake = input().strip()

count_o = snake.count('o')
for _ in range(N):
    if count_o < 2:
        break
    count_o = 3 * count_o - 2

print(count_o)