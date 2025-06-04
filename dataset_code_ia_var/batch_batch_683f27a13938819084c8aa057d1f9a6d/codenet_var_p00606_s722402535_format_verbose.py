# Directions for movement: up, right, down, left
movement_directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

while True:

    number_of_steps = int(input())

    if number_of_steps == 0:
        break

    start_label, target_label, blocked_label = input().split()

    start_position = ord(start_label) - ord('A')
    target_position = ord(target_label) - ord('A')
    blocked_position = ord(blocked_label) - ord('A')

    # Dynamic programming array to store probabilities
    # Dimensions: time_step, row, column
    probability_grid = [[[0.0 for column in range(3)] for row in range(3)] for time_step in range(17)]

    start_row = start_position // 3
    start_column = start_position % 3
    probability_grid[0][start_row][start_column] = 1.0

    for current_step in range(1, number_of_steps + 1):
        for row in range(3):
            for column in range(3):
                for direction in movement_directions:
                    next_row = row + direction[0]
                    next_column = column + direction[1]

                    blocked_row = blocked_position // 3
                    blocked_column = blocked_position % 3

                    # Check if the next cell is out of grid or is blocked
                    if (
                        next_row < 0 or next_row >= 3 or
                        next_column < 0 or next_column >= 3 or
                        (next_row == blocked_row and next_column == blocked_column)
                    ):
                        next_row = row
                        next_column = column

                    probability_grid[current_step][next_row][next_column] += (
                        probability_grid[current_step - 1][row][column] / 4
                    )

    target_row = target_position // 3
    target_column = target_position % 3
    print(probability_grid[number_of_steps][target_row][target_column])