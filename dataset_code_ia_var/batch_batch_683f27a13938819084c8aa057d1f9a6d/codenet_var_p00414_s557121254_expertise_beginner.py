l, n = input().split()
l = int(l)
n = int(n)
maru = 0
snake = input()
for i in range(l - 1):
    if snake[i] == 'o' and snake[i + 1] == 'o':
        maru = maru + 1
for i in range(n):
    l = l + maru * 3
    maru = maru * 2
print(l)