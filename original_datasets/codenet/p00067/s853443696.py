def fill(x, y, board):
    board[y][x] = 2
    points = [[y, x + 1], [y, x - 1], [y + 1, x], [y - 1, x]]

    if y == 0:
        points.remove([y-1, x])
    elif y == 11:
        points.remove([y+1, x])
    if x == 0:
        points.remove([y, x - 1])
    elif x == 11:
        points.remove([y, x + 1])

    for p in points:
        if board[p[0]][p[1]] == 1:
            board = fill(p[1], p[0], board)
    return board

while True:
    try:
        islands = [list(map(int, list(input()))) for i in range(12)]
        ans = 0

        for y in range(12):
            for x in range(12):
                if islands[y][x] == 1:
                    islands = fill(x, y, islands)
                    ans += 1
        print(ans)
        input()
    except:
        break