grid_size = 2001
coverage_grid = [[0 for col_index in range(grid_size)] for row_index in range(grid_size)]

rectangle1_x, rectangle1_y, rectangle1_width, rectangle1_height = [int(value) for value in input().split()]
rectangle2_x, rectangle2_y, rectangle2_width, rectangle2_height = [int(value) for value in input().split()]

covered_area_count = 0

for row in range(rectangle1_x, rectangle1_x + rectangle1_width):
    for col in range(rectangle1_y, rectangle1_y + rectangle1_height):
        coverage_grid[row][col] = 1
        covered_area_count += 1

for row in range(rectangle2_x, rectangle2_x + rectangle2_width):
    for col in range(rectangle2_y, rectangle2_y + rectangle2_height):
        if coverage_grid[row][col] == 0:
            coverage_grid[row][col] = 1
            covered_area_count += 1
        else:
            coverage_grid[row][col] = 0
            covered_area_count -= 1

print(covered_area_count)