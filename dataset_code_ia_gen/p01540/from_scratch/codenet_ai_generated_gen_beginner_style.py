n, m = map(int, input().split())
treasures = []
for _ in range(n):
    x, y = map(int, input().split())
    treasures.append((x, y))

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    count = 0
    for x, y in treasures:
        if x1 <= x <= x2 and y1 <= y <= y2:
            count += 1
    print(count)