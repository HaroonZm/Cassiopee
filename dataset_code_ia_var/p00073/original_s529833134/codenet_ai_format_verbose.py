while True:

    base_input = input()
    height_input = input()

    if base_input == 0 and height_input == 0:
        break

    base_length = float(base_input)
    height_length = float(height_input)

    half_base_length = base_length / 2

    slant_height = (half_base_length ** 2 + height_length ** 2) ** 0.5

    surface_area = base_length * base_length + 2 * base_length * slant_height

    print(surface_area)