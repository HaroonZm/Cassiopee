l,n = map(int,input().split())
maru = 0
snake = input()
for i in range(l-1):
    if snake[i:i+2] == "oo":
        maru += 1
for i in range(n):
    l += maru*3
    maru *= 2
print(l)