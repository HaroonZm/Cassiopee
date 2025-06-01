from itertools import product

MOVES = [(dx, dy) for dx in (-2, -1, 0, 1, 2) for dy in (-2, -1, 0, 1, 2)
         if (abs(dx), abs(dy)) in {(2,1), (1,2), (2,0), (0,2)}]

def search(table, x, y, depth, max_depth):
    if depth == max_depth:
        return True
    if not (0 <= x < 10 and 0 <= y < 10) or table[x][y][depth] == 0:
        return False
    return any(search(table, x+dx, y+dy, depth+1, max_depth) for dx, dy in MOVES)

while (px := py := None) is None or True:
    line = input().strip()
    if not line:
        continue
    px, py = map(int, line.split())
    if (px, py) == (0, 0):
        break
    n = int(input())
    coords = list(map(int, input().split()))
    table = [[[0]*10 for _ in range(10)] for _ in range(10)]
    for d, (x, y) in enumerate(zip(coords[::2], coords[1::2])):
        for dx, dy in product((-1,0,1), repeat=2):
            nx, ny = min(max(x+dx,0),9), min(max(y+dy,0),9)
            table[nx][ny][d] = 1
    print("OK" if search(table, px, py, -1, n) else "NA")