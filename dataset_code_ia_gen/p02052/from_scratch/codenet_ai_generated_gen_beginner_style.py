H, W = map(int, input().split())
campus = [input() for _ in range(H)]

buildings = []
for i in range(H):
    for j in range(W):
        if campus[i][j] == 'B':
            buildings.append((i, j))

max_distance = 0
for b1 in buildings:
    for b2 in buildings:
        dist = abs(b1[0] - b2[0]) + abs(b1[1] - b2[1])
        if dist > max_distance:
            max_distance = dist

print(max_distance)