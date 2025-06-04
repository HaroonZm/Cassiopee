number_of_bits = int(input())

for current_number in range(1 << number_of_bits):

    output_representation = [str(current_number) + ":"]

    for bit_position in range(number_of_bits):

        if (current_number & (1 << bit_position)) != 0:

            output_representation.append(bit_position)

    print(*output_representation)