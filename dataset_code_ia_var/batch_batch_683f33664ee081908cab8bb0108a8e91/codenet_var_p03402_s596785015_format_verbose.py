import numpy as np

number_of_rows_in_half = 24
number_of_columns_in_half = 49

# Initialize the grid with '.' representing white space
full_grid_height = 2 * number_of_columns_in_half + 1
full_grid_width = 2 * (number_of_rows_in_half + number_of_rows_in_half + 1)
grid = np.full((full_grid_height, full_grid_width), '.', dtype='U1')

# Read A and B (the numbers of white and black regions)
number_of_white_regions, number_of_black_regions = map(int, input().split())

# Divide the grid into left (white base) and right (black base) areas
left_area = grid[:, :number_of_rows_in_half + number_of_rows_in_half + 1]
right_area = grid[:, number_of_rows_in_half + number_of_rows_in_half + 1:]
right_area[:] = '#'  # Fill right_area with black

# For both regions, fill patches for the alternate color
for fill_symbol, patches_to_fill, target_area in [
    ['#', number_of_black_regions - 1, left_area],
    ['.', number_of_white_regions - 1, right_area]
]:
    full_patch_rows, left_patches = divmod(patches_to_fill, number_of_rows_in_half)
    for row_index in range(full_patch_rows):
        # Set appropriate patches in a whole row
        target_area[2 * row_index + 1, 1::2] = fill_symbol
    # Fill any remaining patches
    target_area[2 * full_patch_rows + 1, 1:1 + 2 * left_patches:2] = fill_symbol

# Print the final grid size and the visual pattern
total_output_height = full_grid_height
total_output_width = full_grid_width
print(total_output_height, total_output_width)
for row_content in grid:
    print(''.join(row_content))