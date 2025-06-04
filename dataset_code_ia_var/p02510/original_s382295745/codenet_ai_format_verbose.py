while True:

    input_string = raw_input()

    if input_string == "-":
        break

    number_of_rotations = int(raw_input())

    for rotation_index in range(number_of_rotations):

        rotation_amount = int(raw_input())

        input_string = input_string[rotation_amount:] + input_string[:rotation_amount]

    print(input_string)