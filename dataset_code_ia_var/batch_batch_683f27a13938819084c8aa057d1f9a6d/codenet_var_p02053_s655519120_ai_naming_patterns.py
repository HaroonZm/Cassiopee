height, width = map(int, input().split())
grid_matrix = [list(input()) for row_index in range(height)]

black_cell_positions = []

for row_idx in range(height):
    for col_idx in range(width):
        if grid_matrix[row_idx][col_idx] == "B":
            black_cell_positions.append([row_idx, col_idx])

black_cell_positions.sort(key=lambda position: position[0] + position[1])
max_manhattan_distance = abs(black_cell_positions[0][0] - black_cell_positions[-1][0]) + abs(black_cell_positions[0][1] - black_cell_positions[-1][1])

black_cell_positions.sort(key=lambda position: position[0] - position[1])
max_manhattan_distance = max(
    max_manhattan_distance,
    abs(black_cell_positions[0][0] - black_cell_positions[-1][0]) +
    abs(black_cell_positions[0][1] - black_cell_positions[-1][1])
)

print(max_manhattan_distance)