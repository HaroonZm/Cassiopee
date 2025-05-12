n = int(input())

for _ in range(n):
    x1, y1, w, h = map(int, input().split())
    x2 = x1 + w
    y2 = y1 + h

    m = int(input())
    cnt = 0
    for _ in range(m):
        x, y = map(int, input().split())
        if x1 <= x <= x2 and y1 <= y <= y2:
            cnt += 1

    print(cnt)