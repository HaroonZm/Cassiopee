height = 0
width = 0
num_obstacles = 0
while True:
    height, width = map(int, input().split())
    if height == 0 and width == 0:
        break
    height -= 1
    width -= 1
    obstacles = [[1] * (width + 1) for _ in range(height + 1)]
    num_obstacles = int(input())
    for _ in range(num_obstacles):
        x_pos, y_pos = map(int, input().split())
        obstacles[x_pos - 1][y_pos - 1] = 0
    dp_table = [[0] * (width + 2) for _ in range(height + 2)]
    dp_table[0][0] = obstacles[0][0]
    for row_index in range(height + 1):
        for col_index in range(width + 1):
            if obstacles[row_index][col_index]:
                dp_table[row_index + 1][col_index] += dp_table[row_index][col_index]
                dp_table[row_index][col_index + 1] += dp_table[row_index][col_index]
    if obstacles[height][width]:
        print(dp_table[height][width])
    else:
        print(0)