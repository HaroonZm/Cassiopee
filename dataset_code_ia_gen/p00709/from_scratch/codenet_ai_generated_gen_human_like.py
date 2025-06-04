def can_place_carpet(floor, x, y, size, W, H):
    if x + size > W or y + size > H:
        return False
    for i in range(y, y + size):
        for j in range(x, x + size):
            if floor[i][j] == 0:
                return False
    return True

def place_carpet(floor, x, y, size, val):
    for i in range(y, y + size):
        for j in range(x, x + size):
            floor[i][j] = val

def find_first_scratched(floor, W, H):
    for y in range(H):
        for x in range(W):
            if floor[y][x] == 1:
                return x, y
    return -1, -1

def backtrack(floor, W, H, count, memo):
    key = tuple(tuple(row) for row in floor)
    if key in memo:
        if memo[key] <= count:
            return float('inf')
    memo[key] = count
    x, y = find_first_scratched(floor, W, H)
    if x == -1 and y == -1:
        return count
    res = float('inf')
    max_size = min(W - x, H - y)
    # Try placing largest possible carpet first to reduce carpets count
    for size in reversed(range(1, max_size + 1)):
        if can_place_carpet(floor, x, y, size, W, H):
            place_carpet(floor, x, y, size, 0)
            res = min(res, backtrack(floor, W, H, count + 1, memo))
            place_carpet(floor, x, y, size, 1)
    return res

def main():
    while True:
        W, H = map(int, input().split())
        if W == 0 and H == 0:
            break
        floor = [list(map(int, input().split())) for _ in range(H)]
        result = backtrack(floor, W, H, 0, dict())
        print(result)

if __name__ == "__main__":
    main()