while True:

    number_of_rotations = input()

    if number_of_rotations == 0:
        break

    faces_indices = range(1, 7)
    current_die_faces = list(faces_indices)

    for rotation_index in range(number_of_rotations):

        rotation_command = raw_input()[0]

        if rotation_command == "s":
            rotation_mapping = [1, 5, 2, 3, 0, 4]
        elif rotation_command == "n":
            rotation_mapping = [4, 0, 2, 3, 5, 1]
        elif rotation_command == "w":
            rotation_mapping = [3, 1, 0, 5, 4, 2]
        elif rotation_command == "e":
            rotation_mapping = [2, 1, 5, 0, 4, 3]

        current_die_faces = [current_die_faces[mapped_index] for mapped_index in rotation_mapping]

    print current_die_faces[0]