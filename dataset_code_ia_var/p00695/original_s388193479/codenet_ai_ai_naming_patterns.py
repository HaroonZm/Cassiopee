WIDTH = HEIGHT = 5
num_cases = input()
for case_index in range(num_cases):
    input_matrix = [map(int, raw_input().split()) for row_index in range(HEIGHT)]
    consecutive_ones_row = [[0] * WIDTH for row_index in range(HEIGHT)]
    consecutive_ones_rect = [[0] * WIDTH for row_index in range(HEIGHT)]
    max_area = 1
    for row in range(HEIGHT):
        current_row_streak = 0
        for col in range(WIDTH):
            if input_matrix[row][col] == 1:
                current_row_streak += 1
            else:
                current_row_streak = 0
            consecutive_ones_row[row][col] = current_row_streak
            consecutive_ones_rect[row][col] = (consecutive_ones_rect[row-1][col] if row > 0 else 0) + 1 if current_row_streak > 0 else 0
            if current_row_streak * consecutive_ones_rect[row][col] > max_area:
                min_width = current_row_streak
                for rect_height in range(consecutive_ones_rect[row][col]):
                    min_width = min(min_width, consecutive_ones_row[row-rect_height][col])
                    if min_width * consecutive_ones_rect[row][col] <= max_area:
                        break
                    max_area = max(max_area, min_width * (rect_height + 1))
    print max_area
    if case_index != num_cases - 1:
        raw_input()