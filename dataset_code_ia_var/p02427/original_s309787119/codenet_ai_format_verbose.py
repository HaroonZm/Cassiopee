if __name__ == "__main__":

    number_of_bits = int(input())

    print("0:")

    for current_integer in range(1, 2 ** number_of_bits):

        print(f"{current_integer}: ", end="")

        set_bit_positions = [
            str(bit_position)
            for bit_position in range(number_of_bits)
            if current_integer & (1 << bit_position)
        ]

        print(" ".join(set_bit_positions))