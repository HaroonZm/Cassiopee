t = int(input())
for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))
    max_up = 0
    max_down = 0
    for i in range(1, n):
        diff = h[i] - h[i-1]
        if diff > 0:
            if diff > max_up:
                max_up = diff
        else:
            diff = -diff
            if diff > max_down:
                max_down = diff
    print(max_up, max_down)