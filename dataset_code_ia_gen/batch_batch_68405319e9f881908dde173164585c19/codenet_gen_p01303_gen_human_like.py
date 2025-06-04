t = int(input())
for _ in range(t):
    X, Y, W, H = map(int, input().split())
    N = int(input())
    count = 0
    for __ in range(N):
        x, y = map(int, input().split())
        if X <= x <= X + W and Y <= y <= Y + H:
            count += 1
    print(count)