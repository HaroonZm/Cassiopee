def solve():
    
    height, width = map(int, input().split())
    
    if height == 0:
        return False

    map_grid = [input() for _ in range(height)]
    
    consecutive_dots_count = [[0] * width for _ in range(height)]
    
    for col_index in range(width):
        dot_streak = 0
        for row_index in range(height - 1, -1, -1):
            if map_grid[row_index][col_index] == '.':
                dot_streak += 1
            else:
                dot_streak = 0
            consecutive_dots_count[row_index][col_index] = dot_streak

    maximum_area = 0
    
    for row_index in range(height):
        stack = [(0, -1)]
        for col_index in range(width):
            current_height = consecutive_dots_count[row_index][col_index]
            last_position = col_index

            while stack and current_height <= stack[-1][0]:
                popped_height, popped_position = stack.pop()
                area = (col_index - popped_position) * popped_height
                maximum_area = max(maximum_area, area)
                last_position = popped_position
            
            stack.append((current_height, last_position))
        
        while stack:
            popped_height, popped_position = stack.pop()
            area = (width - popped_position) * popped_height
            maximum_area = max(maximum_area, area)

    print(maximum_area)
    return True


while solve():
    pass