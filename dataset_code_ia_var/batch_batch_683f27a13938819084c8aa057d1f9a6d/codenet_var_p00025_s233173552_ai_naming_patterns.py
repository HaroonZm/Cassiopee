def input_lines_generator():
    while True:
        try:
            line = input()
            yield line
        except EOFError:
            break

input_lines_list = list(input_lines_generator())
for index in range(0, len(input_lines_list), 2):
    sequence_a_str = input_lines_list[index]
    sequence_b_str = input_lines_list[index + 1]
    sequence_a = [int(element) for element in sequence_a_str.split()]
    sequence_b = [int(element) for element in sequence_b_str.split()]

    match_count_exact = 0
    match_count_partial = 0
    for position_a in range(len(sequence_a)):
        for position_b in range(len(sequence_b)):
            if sequence_a[position_a] == sequence_b[position_b]:
                if position_a == position_b:
                    match_count_exact += 1
                else:
                    match_count_partial += 1
    print(match_count_exact, match_count_partial)