#!/usr/bin/python3

def main():

    DIRECTION_LEFT = 0
    DIRECTION_RIGHT = 1
    DIRECTION_UP = 2
    DIRECTION_DOWN = 3

    grid_height, grid_width, number_of_moves = map(int, input().split())

    start_row, start_column = map(int, input().split())
    # Convert to 0-based indexing
    current_row = start_row - 1
    current_column = start_column - 1

    player_moves = input().strip()[::-1]
    obstacle_moves = input().strip()[::-1]

    movement_bounds = [
        0,                # leftmost column
        grid_width - 1,   # rightmost column
        0,                # uppermost row
        grid_height - 1   # lowermost row
    ]

    def move_player(direction):

        if direction == 'L':
            movement_bounds[DIRECTION_LEFT] = min(max(-1, movement_bounds[DIRECTION_LEFT] + 1), grid_width)
        if direction == 'R':
            movement_bounds[DIRECTION_RIGHT] = min(max(-1, movement_bounds[DIRECTION_RIGHT] - 1), grid_width)
        if direction == 'U':
            movement_bounds[DIRECTION_UP] = min(max(-1, movement_bounds[DIRECTION_UP] + 1), grid_height)
        if direction == 'D':
            movement_bounds[DIRECTION_DOWN] = min(max(-1, movement_bounds[DIRECTION_DOWN] - 1), grid_height)

    def move_obstacle(direction):

        if direction == 'L':
            movement_bounds[DIRECTION_RIGHT] = min(max(0, movement_bounds[DIRECTION_RIGHT] + 1), grid_width - 1)
        if direction == 'R':
            movement_bounds[DIRECTION_LEFT] = min(max(0, movement_bounds[DIRECTION_LEFT] - 1), grid_width - 1)
        if direction == 'U':
            movement_bounds[DIRECTION_DOWN] = min(max(0, movement_bounds[DIRECTION_DOWN] + 1), grid_height - 1)
        if direction == 'D':
            movement_bounds[DIRECTION_UP] = min(max(0, movement_bounds[DIRECTION_UP] - 1), grid_height - 1)

    def is_out_of_bounds():

        if (
            movement_bounds[DIRECTION_LEFT] > movement_bounds[DIRECTION_RIGHT] or
            movement_bounds[DIRECTION_LEFT] < 0 or
            movement_bounds[DIRECTION_RIGHT] > grid_width - 1
        ):
            return True

        if (
            movement_bounds[DIRECTION_UP] > movement_bounds[DIRECTION_DOWN] or
            movement_bounds[DIRECTION_UP] < 0 or
            movement_bounds[DIRECTION_DOWN] > grid_height - 1
        ):
            return True

        return False

    for player_direction, obstacle_direction in zip(player_moves, obstacle_moves):

        move_obstacle(obstacle_direction)
        move_player(player_direction)

        if is_out_of_bounds():
            print('NO')
            return

    if (
        movement_bounds[DIRECTION_LEFT] <= current_column <= movement_bounds[DIRECTION_RIGHT] and
        movement_bounds[DIRECTION_UP] <= current_row <= movement_bounds[DIRECTION_DOWN]
    ):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()