main_grid_height, main_grid_width = (int(value) for value in input().split())
sub_grid_height, sub_grid_width = (int(value) for value in input().split())
remaining_area = (main_grid_height - sub_grid_height) * (main_grid_width - sub_grid_width)
print(remaining_area)