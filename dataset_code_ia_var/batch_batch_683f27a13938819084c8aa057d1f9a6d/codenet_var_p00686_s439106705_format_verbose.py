# AOJ 1104: Where's Your Robot? (Version à haute lisibilité, noms explicites)

# Déplacements possibles pour chaque direction : Nord, Est, Sud, Ouest (ordre : x, y)
direction_forward_moves = [
    [0, 1],   # Nord : avancer sur y positif
    [1, 0],   # Est  : avancer sur x positif
    [0, -1],  # Sud  : avancer sur y négatif
    [-1, 0],  # Ouest: avancer sur x négatif
]

direction_backward_moves = [
    [0, -1],  # Nord : reculer sur y négatif
    [-1, 0],  # Est  : reculer sur x négatif
    [0, 1],   # Sud  : reculer sur y positif
    [1, 0],   # Ouest: reculer sur x positif
]

while True:

    grid_width, grid_height = map(int, input().split())

    if grid_width == 0:
        break

    robot_x = 1
    robot_y = 1
    robot_direction = 0   # 0: Nord, 1: Est, 2: Sud, 3: Ouest

    while True:

        command_line = input().split()
        command = command_line[0]

        if command == "STOP":
            break

        elif command == "RIGHT":
            robot_direction = (robot_direction + 1) % 4

        elif command == "LEFT":
            robot_direction = (robot_direction + 3) % 4

        else:
            steps = int(command_line[1])

            if command == "FORWARD":
                move_x = direction_forward_moves[robot_direction][0] * steps
                move_y = direction_forward_moves[robot_direction][1] * steps

            else:  # BACKWARD
                move_x = direction_backward_moves[robot_direction][0] * steps
                move_y = direction_backward_moves[robot_direction][1] * steps

            new_robot_x = robot_x + move_x
            new_robot_y = robot_y + move_y

            # Gestion des limites de la grille
            if new_robot_x < 1:
                new_robot_x = 1
            if new_robot_x > grid_width:
                new_robot_x = grid_width

            if new_robot_y < 1:
                new_robot_y = 1
            if new_robot_y > grid_height:
                new_robot_y = grid_height

            robot_x = new_robot_x
            robot_y = new_robot_y

    print(robot_x, robot_y)