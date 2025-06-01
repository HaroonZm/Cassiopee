H, W = map(int, input().split())
field = [list(input()) for _ in range(H)]

def count_surrounding_empty(r, c):
    cnt = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            nr, nc = r+dr, c+dc
            if field[nr][nc] == '.':
                cnt += 1
    return cnt

waves = 0
while True:
    to_destroy = []
    for i in range(1, H-1):
        for j in range(1, W-1):
            if field[i][j] == '.':
                continue
            strength = int(field[i][j])
            empty_count = count_surrounding_empty(i, j)
            if empty_count >= strength:
                to_destroy.append((i, j))
    if not to_destroy:
        break
    for r, c in to_destroy:
        field[r][c] = '.'
    waves += 1

print(waves)