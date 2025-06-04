H, R = map(int, input().split())

top = H + R

if top > 0:
    print(1)
elif top == 0:
    print(0)
else:
    print(-1)