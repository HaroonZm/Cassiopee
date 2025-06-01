import fileinput

CHARACTER_MASTER_TABLE = [
    ' ', '\',.!?', 'abcABC', 'defDEF', 'ghiGHI',
    'jklJKL', 'mnoMNO', 'pqrsPQRS', 'tuvTUV', 'wxyzWXYZ'
]

for raw_line in (input_line.strip() for input_line in fileinput.input()):
    processed_line = raw_line + '!'
    previous_char = None
    repetition_count = 0
    decoded_characters = []
    for current_char in processed_line:
        if current_char == previous_char:
            repetition_count += 1
            continue
        if previous_char == '0':
            if repetition_count > 1:
                decoded_characters.extend([(0, 0)] * (repetition_count - 1))
        else:
            if previous_char is not None:
                decoded_characters.append((int(previous_char), repetition_count - 1))
        previous_char = current_char
        repetition_count = 1
    print(''.join(CHARACTER_MASTER_TABLE[index][pos] for index, pos in decoded_characters))