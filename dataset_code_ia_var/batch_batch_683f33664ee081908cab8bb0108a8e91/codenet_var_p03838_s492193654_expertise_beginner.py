x, y = input().split()
x = int(x)
y = int(y)
ans = 10 ** 18

if y - x > 0:
    if y - x < ans:
        ans = y - x

if -x <= y:
    if 1 + y + x < ans:
        ans = 1 + y + x

if x <= -y:
    if 1 + -y - x < ans:
        ans = 1 + -y - x

if -x <= -y:
    if 2 + -y + x < ans:
        ans = 2 + -y + x

print(ans)