while True:

    rectangle_base_length = int(input())
    rectangle_height = int(input())

    if rectangle_base_length == 0 and rectangle_height == 0:
        break

    rectangle_diagonal_length = (rectangle_height ** 2 + (rectangle_base_length / 2) ** 2) ** 0.5

    rectangle_area_plus_side_areas = (
        rectangle_base_length * rectangle_base_length +
        rectangle_base_length * rectangle_diagonal_length * 2
    )

    print(rectangle_area_plus_side_areas)