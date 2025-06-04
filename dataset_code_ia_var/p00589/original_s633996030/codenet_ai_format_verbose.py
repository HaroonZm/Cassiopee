import fileinput

character_mappings_per_keypress = [
    ' ',                     # 0
    '\',.!?',                # 1
    'abcABC',                # 2
    'defDEF',                # 3
    'ghiGHI',                # 4
    'jklJKL',                # 5
    'mnoMNO',                # 6
    'pqrsPQRS',              # 7
    'tuvTUV',                # 8
    'wxyzWXYZ'               # 9
]

for input_line_stripped in (line.strip() for line in fileinput.input()):
    
    input_line_with_sentinel = input_line_stripped + '!'
    
    previous_character = None
    consecutive_count = 0
    pressed_keys_and_counts = []
    
    for current_character in input_line_with_sentinel:
        
        if current_character == previous_character:
            consecutive_count += 1
            continue
        
        if previous_character == '0':
            if consecutive_count > 1:
                pressed_keys_and_counts.extend( [(0, 0)] * (consecutive_count - 1) )
        else:
            if previous_character is not None:
                pressed_keys_and_counts.append(
                    (int(previous_character), consecutive_count - 1)
                )
        
        previous_character = current_character
        consecutive_count = 1

    output_characters = ''.join(
        character_mappings_per_keypress[digit][index]
        for digit, index in pressed_keys_and_counts
    )
    print(output_characters)