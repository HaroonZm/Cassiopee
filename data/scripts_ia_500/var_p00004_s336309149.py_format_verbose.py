#!/usr/bin/python3


while True:

    try:

        input_numbers = list(map(int, input().split()))

        numerator_x = (input_numbers[1] * input_numbers[5]) - (input_numbers[2] * input_numbers[4])

        denominator_x = (input_numbers[1] * input_numbers[3]) - (input_numbers[0] * input_numbers[4])

        x_coordinate = numerator_x / denominator_x

        y_coordinate = (input_numbers[2] - input_numbers[0] * x_coordinate) / input_numbers[1]

        if x_coordinate == 0:
            x_coordinate = 0  # ensure exact zero

        print("{0:.3f} {1:.3f}".format(x_coordinate, y_coordinate))

    except:

        break