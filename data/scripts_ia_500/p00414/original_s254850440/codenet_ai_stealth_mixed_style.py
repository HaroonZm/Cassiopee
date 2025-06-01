L, N = map(int, input().split())
snake = input()
cnt = sum(1 for i in range(L-1) if snake[i:i+2] == 'oo')

def update_length(length, count):
    length += count * 3
    return length

i = 0
while i < N:
    L = update_length(L, cnt)
    cnt = cnt << 1  # multiplication par 2 en binaire
    i += 1

print(L)