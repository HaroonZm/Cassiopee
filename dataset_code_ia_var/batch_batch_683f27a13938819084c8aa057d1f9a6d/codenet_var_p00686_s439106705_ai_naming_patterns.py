# AOJ 1104: Where's Your Robot?
# Python3 2018.7.14 bal4u (refactor: systematic naming)

DIRECTION_FORWARD_VECTORS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
DIRECTION_BACKWARD_VECTORS = [[0, -1], [-1, 0], [0, 1], [1, 0]]

while True:
    grid_width, grid_height = map(int, input().split())
    if grid_width == 0:
        break
    robot_row, robot_col, robot_dir = 1, 1, 0
    while True:
        command_parts = input().split()
        command_name = command_parts[0]
        if command_name == "STOP":
            break
        elif command_name == "RIGHT":
            robot_dir = (robot_dir + 1) % 4
        elif command_name == "LEFT":
            robot_dir = (robot_dir + 3) % 4
        else:
            move_distance = int(command_parts[1])
            if command_name == "FORWARD":
                next_row = robot_row + move_distance * DIRECTION_FORWARD_VECTORS[robot_dir][1]
                next_col = robot_col + move_distance * DIRECTION_FORWARD_VECTORS[robot_dir][0]
            else:  # BACKWARD
                next_row = robot_row + move_distance * DIRECTION_BACKWARD_VECTORS[robot_dir][1]
                next_col = robot_col + move_distance * DIRECTION_BACKWARD_VECTORS[robot_dir][0]
            if next_row < 1:
                next_row = 1
            if next_row > grid_height:
                next_row = grid_height
            if next_col < 1:
                next_col = 1
            if next_col > grid_width:
                next_col = grid_width
            robot_row, robot_col = next_row, next_col
    print(robot_col, robot_row)