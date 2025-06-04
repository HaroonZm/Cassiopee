while True:

    input_height, input_width = map(int, raw_input().split())

    if input_height == 0 and input_width == 0:
        break

    else:

        top_and_bottom_border = '#' * input_width + '\n'
        if input_height > 2:
            middle_section = ('#' + '.' * (input_width - 2) + '#' + '\n') * (input_height - 2)
        else:
            middle_section = ''
        rectangle_pattern = (
            top_and_bottom_border +
            middle_section +
            top_and_bottom_border
        )

        print(rectangle_pattern)