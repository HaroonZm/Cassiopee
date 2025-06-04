while True:
    n = input()
    if n == '0':
        break
    n = int(n)
    grid = []
    for _ in range(n):
        row = input()
        grid.append(row)

    max_count = 0

    for i in range(n):
        for j in range(n):
            if grid[i][j] == '1':
                # horizontal
                count = 0
                for k in range(j, n):
                    if grid[i][k] == '1':
                        count += 1
                    else:
                        break
                if count > max_count:
                    max_count = count

                # vertical
                count = 0
                for k in range(i, n):
                    if grid[k][j] == '1':
                        count += 1
                    else:
                        break
                if count > max_count:
                    max_count = count

                # diagonal down-right
                count = 0
                x, y = i, j
                while x < n and y < n and grid[x][y] == '1':
                    count += 1
                    x += 1
                    y += 1
                if count > max_count:
                    max_count = count

                # diagonal down-left
                count = 0
                x, y = i, j
                while x < n and y >= 0 and grid[x][y] == '1':
                    count += 1
                    x += 1
                    y -= 1
                if count > max_count:
                    max_count = count

    print(max_count)