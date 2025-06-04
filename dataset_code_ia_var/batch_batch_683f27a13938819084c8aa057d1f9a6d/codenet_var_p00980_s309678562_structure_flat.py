COLS, ROWS, N = list(map(int, input().split()))

board = [ [ None for _ in range(COLS) ] for _ in range(ROWS) ]
plist = []

adjR = [-1, 0, 0, 1]
adjC = [0, -1, 1, 0]

given = set()

for _ in range(N):
    c, r, h = list(map(int, input().strip().split()))
    board[r - 1][c - 1] = h
    plist.append((r-1, c-1))
    given.add((r-1, c-1))

while len(plist) > 0:
    row, col = plist.pop(0)
    h = board[row][col]
    for i in range(4):
        rr = row + adjR[i]
        cc = col + adjC[i]
        if (rr, cc) in given:
            continue
        if rr >= 0 and rr < ROWS and cc >= 0 and cc < COLS:
            if board[rr][cc] is None or board[rr][cc] < h - 1:
                board[rr][cc] = h - 1
                plist.append((rr, cc))

isPossible = True
total = 0
for r in range(ROWS):
    for c in range(COLS):
        h = board[r][c]
        for i in range(4):
            rr = r + adjR[i]
            cc = c + adjC[i]
            if rr >= 0 and rr < ROWS and cc >= 0 and cc < COLS:
                diff = abs(h - board[rr][cc])
                if diff > 1:
                    isPossible = False
                    break
        if not isPossible:
            break
        total += h
    if not isPossible:
        break

print(total if isPossible else "No")