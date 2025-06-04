height_value, width_value, offset_x_value, offset_y_value = map(int, input().split())

product_area = height_value * width_value
sum_offsets = offset_x_value + offset_y_value
total_result = product_area * sum_offsets

if total_result % 2 == 1:
    print('No')
else:
    print('Yes')