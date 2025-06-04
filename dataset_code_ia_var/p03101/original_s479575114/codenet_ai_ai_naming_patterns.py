main_grid_height, main_grid_width = map(int, input().split())
sub_grid_height, sub_grid_width = map(int, input().split())
main_grid_area = main_grid_height * main_grid_width
border_cells_area = sub_grid_height * main_grid_width + sub_grid_width * main_grid_height - sub_grid_height * sub_grid_width
answer = main_grid_area - border_cells_area
print(answer)