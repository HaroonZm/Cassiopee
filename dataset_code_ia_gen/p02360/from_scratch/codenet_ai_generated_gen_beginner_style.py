n = int(input())
seals = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    seals.append((x1, y1, x2, y2))

# On crée une grille de 1001x1001 initialisée à zero
grid = [[0]*1001 for _ in range(1001)]

for seal in seals:
    x1, y1, x2, y2 = seal
    for x in range(x1, x2):
        for y in range(y1, y2):
            grid[x][y] += 1

max_overlap = 0
for x in range(1001):
    for y in range(1001):
        if grid[x][y] > max_overlap:
            max_overlap = grid[x][y]

print(max_overlap)