char_table = ["", "',.!?", "abcABC", "defDEF", "ghiGHI", "jklJKL",
              "mnoMNO", "pqrsPQRS", "tuvTUV", "wxyzWXYZ"]

while True:
    try:
        input_string = input().strip()
    except EOFError:
        break

    decoded_string = ''
    index = 0
    while index < len(input_string):
        current_char = input_string[index]
        count = 0
        digit = int(current_char)
        index += 1
        while index < len(input_string) and input_string[index] == current_char:
            index += 1
            count += 1
        if digit == 0:
            decoded_string += ' ' * count
        else:
            decoded_string += char_table[digit][count % len(char_table[digit])]
    print(decoded_string)