while True:
    height, width = map(int, raw_input().split())
    if height == 0 and width == 0:
        break
    row_indices = range(height)
    column_count = [0] * (height + 1)
    max_rect_width = column_count[:]
    prev_column_heights = [0] * width
    for row_index in row_indices:
        row_string = raw_input()
        current_column_heights = [0] * width
        span_pointer = -1
        column_positions = [-1] * (height + 1)
        for col_index in range(width):
            if row_string[col_index] == "*":
                contiguous_height = 0
            elif row_string[col_index] == ".":
                contiguous_height = prev_column_heights[col_index] + 1
            current_column_heights[col_index] = contiguous_height
            if contiguous_height > span_pointer:
                fill_start = span_pointer + 1
                fill_end = contiguous_height + 1
                column_positions[fill_start:fill_end] = [col_index] * (fill_end - fill_start)
            elif contiguous_height < span_pointer:
                for k in range(contiguous_height + 1, span_pointer + 1):
                    max_rect_width[k] = max(max_rect_width[k], col_index - column_positions[k])
                    column_positions[k] = -1
            span_pointer = contiguous_height
        for k in range(1, span_pointer + 1):
            if column_positions[k] >= 0:
                max_rect_width[k] = max(max_rect_width[k], width - column_positions[k])
        prev_column_heights = current_column_heights[:]
    max_area = max(height_segment * max_rect_width[height_segment] for height_segment in range(height + 1))
    print max_area