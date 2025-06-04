import sys

input_stream_read_line = sys.stdin.readline
output_stream_write = sys.stdout.write

number_of_bits = int(input_stream_read_line())

output_stream_write("0:\n")

for current_integer in range(1, 1 << number_of_bits):

    included_indices = [
        str(bit_position)
        for bit_position in range(number_of_bits)
        if current_integer & (1 << bit_position)
    ]

    output_stream_write(
        "{}: {}\n".format(
            current_integer,
            " ".join(included_indices)
        )
    )