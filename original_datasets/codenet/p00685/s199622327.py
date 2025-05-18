def get_index(fixed):
    for y, f in enumerate(fixed):
        try:
            x = f.index(0)
            return x, y
        except ValueError:
            pass

def recursive(i, fixed):
    if i == 9:
        return 1
    result = 0
    x, y = get_index(fixed)
    fixed[y][x] = i
    for dx, dy in ds:
        x2, y2 = x + dx, y + dy
        if not (0 <= x2 < 4 and 0 <= y2 < 4):
            continue
        if fixed[y2][x2]:
            continue
        fixed[y2][x2] = i
        result += recursive(i + 1, fixed)
        fixed[y2][x2] = 0
    fixed[y][x] = 0
    return result

while True:
    ipt = list(map(int, input().split()))
    if len(ipt) == 1:
        break
    ds = list(zip(*[iter(ipt)] * 2))
    print(recursive(1, [[0] * 4 for _ in range(4)]))