def solve_problem():
    height, width = map(int, input().split())
    if height == 0:
        return False
    map_pattern = [input() for row_index in range(height)]
    count_matrix = [[0] * width for row_index in range(height)]
    for column_index in range(width):
        consecutive_empty = 0
        for row_index in range(height - 1, -1, -1):
            if map_pattern[row_index][column_index] == '.':
                consecutive_empty += 1
            else:
                consecutive_empty = 0
            count_matrix[row_index][column_index] = consecutive_empty
    maximum_area = 0
    for row_index in range(height):
        stack = [(0, -1)]
        for column_index in range(width):
            current_height = count_matrix[row_index][column_index]
            last_position = column_index
            while stack and current_height <= stack[-1][0]:
                height_value, position_index = stack.pop()
                maximum_area = max(maximum_area, (column_index - position_index) * height_value)
                last_position = position_index
            stack.append((current_height, last_position))
        while stack:
            height_value, position_index = stack.pop()
            maximum_area = max(maximum_area, (width - position_index) * height_value)
    print(maximum_area)
    return True

while solve_problem():
    pass