height_value, width_value, pos_x_value, pos_y_value = map(int, input().split())
total_area_value = height_value * width_value
coordinates_sum_value = pos_x_value + pos_y_value
is_area_odd_flag = total_area_value % 2 == 1
is_coordinates_sum_odd_flag = coordinates_sum_value % 2 == 1
result_output_string = 'No' if is_area_odd_flag and is_coordinates_sum_odd_flag else 'Yes'
print(result_output_string)