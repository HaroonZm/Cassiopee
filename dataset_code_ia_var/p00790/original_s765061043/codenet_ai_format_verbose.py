while True:

    nombre_de_rotations = input()

    if nombre_de_rotations == 0:
        break

    faces_du_de = range(1, 7)

    for index_rotation in range(nombre_de_rotations):

        direction_rotation = raw_input()[0]

        if direction_rotation == "s":
            permutation_sud = [1, 5, 2, 3, 0, 4]
            permutation_a_appliquer = permutation_sud
        elif direction_rotation == "n":
            permutation_nord = [4, 0, 2, 3, 5, 1]
            permutation_a_appliquer = permutation_nord
        elif direction_rotation == "w":
            permutation_ouest = [3, 1, 0, 5, 4, 2]
            permutation_a_appliquer = permutation_ouest
        elif direction_rotation == "e":
            permutation_est = [2, 1, 5, 0, 4, 3]
            permutation_a_appliquer = permutation_est

        faces_du_de = [faces_du_de[face_index] for face_index in permutation_a_appliquer]

    print faces_du_de[0]