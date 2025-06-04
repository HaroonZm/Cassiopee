high, width = map(int, input().split())
s_list = [list(input()) for _ in range(high)]
tmp_list = [[0 for _ in range(width)] for _ in range(high)]
directions = [[-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]

for h in range(high):
    for w in range(width):
        if s_list[h][w] == '#':
            tmp_list[h][w] = '#'
            for dx, dy in directions:
                nh = h + dx
                nw = w + dy
                if 0 <= nh < high and 0 <= nw < width:
                    if s_list[nh][nw] == '.':
                        if tmp_list[nh][nw] != '#':
                            tmp_list[nh][nw] += 1

for row in tmp_list:
    output = []
    for cell in row:
        if cell == '#':
            output.append('#')
        else:
            output.append(str(cell))
    print(''.join(output))