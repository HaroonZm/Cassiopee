t = int(input())
for _ in range(t):
    n = int(input())
    heights = list(map(int, input().split()))
    max_up = 0
    max_down = 0
    for i in range(n - 1):
        diff = heights[i + 1] - heights[i]
        if diff > 0:
            if diff > max_up:
                max_up = diff
        else:
            if -diff > max_down:
                max_down = -diff
    print(max_up, max_down)