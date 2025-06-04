height_original, width_original = map(int, input().split())
height_adjusted = height_original + 2
width_adjusted = width_original + 2
for row_index in range(height_adjusted):
    if row_index == 0 or row_index == height_adjusted - 1:
        output_row = "#" * width_adjusted
    else:
        input_row_content = input()
        output_row = "#" + input_row_content + "#"
    print(output_row)