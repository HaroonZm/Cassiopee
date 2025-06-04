def get_index(DATA):
    for y, f in enumerate(DATA):
        try:
            x = f.index(0)
            return x, y
        except ValueError:
            pass

def solve(i, DATA):
    if i == 9:
        return 1
    result = 0
    x1, y1 = get_index(DATA)
    DATA[y1][x1] = i
    for dx, dy in ds:
        x2 = x1 + dx
        y2 = y1 + dy
        if not (0 <= x2 < 4 and 0 <= y2 < 4):
            continue
        if DATA[y2][x2]:
            continue
        DATA[y2][x2] = i
        result += solve(i + 1, DATA)
        DATA[y2][x2] = 0
    DATA[y1][x1] = 0
    return result

while True:
    data = list(map(int, input().split()))
    if len(data) == 1:
        break
    ds = list(zip(*[iter(data)] * 2))
    print(solve(1, [[0] * 4 for _ in range(4)]))