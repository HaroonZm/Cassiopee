number_of_white_areas, number_of_black_areas = map(int, input().split())

white_grid = [["."] * 100 for row_index in range(50)]
black_grid = [["#"] * 100 for row_index in range(50)]

current_x_white = 0
current_y_white = 0

# Place (B-1) black "#" islands into the upper (white) part
for black_area_index in range(number_of_black_areas - 1):

    white_grid[current_y_white][current_x_white] = "#"

    current_x_white += 2

    if current_x_white >= 100:
        current_x_white = 0
        current_y_white += 2

current_x_black = 0
current_y_black = 1

# Place (A-1) white "." islands into the lower (black) part
for white_area_index in range(number_of_white_areas - 1):

    black_grid[current_y_black][current_x_black] = "."

    current_x_black += 2

    if current_x_black >= 100:
        current_x_black = 0
        current_y_black += 2

print(100, 100)

for white_row in white_grid:
    print("".join(white_row))

for black_row in black_grid:
    print("".join(black_row))