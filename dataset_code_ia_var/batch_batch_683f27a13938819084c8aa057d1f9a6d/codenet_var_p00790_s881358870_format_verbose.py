direction_to_index_mapping = {
    's': 1,    # south
    'w': 2,    # west
    'e': 3,    # east
    'n': 4     # north
}

rotation_indices_per_direction = [
    [0, 1, 2, 3, 4, 5, 6],    # Identity (no rotation)
    [0, 2, 6, 3, 4, 1, 5],    # South rotation
    [0, 4, 2, 1, 6, 5, 3],    # West rotation
    [0, 3, 2, 6, 1, 5, 4],    # East rotation
    [0, 5, 1, 3, 4, 6, 2]     # North rotation
]

while True:

    number_of_rotations = int(input())

    if number_of_rotations == 0:
        break

    current_die_face_indices = [face_index for face_index in range(7)]

    for _ in range(number_of_rotations):

        rotation_direction_character = input()[0]

        direction_index = direction_to_index_mapping[rotation_direction_character]

        rotation_sequence = rotation_indices_per_direction[direction_index]

        updated_die_face_indices = [
            current_die_face_indices[rotation_sequence[face_position]]
            for face_position in range(7)
        ]

        current_die_face_indices = updated_die_face_indices

    print(current_die_face_indices[1])