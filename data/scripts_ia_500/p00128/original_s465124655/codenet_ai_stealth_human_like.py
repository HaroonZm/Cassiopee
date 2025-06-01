def get_input():
    while True:
        try:
            # Just read a line and return it as a single string
            yield ''.join(input())
        except EOFError:
            break  # no more input, so break out of the loop

# This table is kinda weird, maybe some pattern printing thing
table = [
    "* = ****",
    "* =* ***",
    "* =** **",
    "* =*** *",
    "* =**** ",
    " *= ****",
    " *=* ***",
    " *=** **",
    " *=*** *",
    " *=**** "
]

inputs = list(get_input())  # grab all inputs first

for idx in range(len(inputs)):
    if idx > 0:
        print()  # blank line between outputs

    number = int(inputs[idx])
    chunks = []

    # Split the number into digits, left to right?
    # Assuming number has up to 5 digits
    for pos in range(5): 
        divisor = 10 ** (4 - pos)
        digit = number // divisor
        chunks.append(table[digit])
        number = number % divisor

    # print pattern lines, 8 lines tall for each digit's representation
    for line_idx in range(8):
        for segment in chunks:
            # print char at current line index
            print(segment[line_idx], end="")
        print()  # newline after each line_idx iterations