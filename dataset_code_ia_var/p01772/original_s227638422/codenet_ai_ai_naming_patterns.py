input_string = raw_input()
if "A" not in input_string:
    print -1
else:
    sequence = "A"
    start_pos = input_string.index("A") + 1
    for current_char in input_string[start_pos:]:
        if sequence[-1] == "A" and current_char == "Z":
            sequence += current_char
        if sequence[-1] == "Z" and current_char == "A":
            sequence += current_char
    if sequence[-1] == "A":
        sequence = sequence[:-1]
    print sequence if sequence else -1