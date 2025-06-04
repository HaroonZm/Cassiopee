def solve():
    input_count = int(input())
    input_values = list(map(int, input().split()))
    pair_list = []

    def append_to_pair_list(element):
        pair_list.append(element)

    for index in range(input_count):
        append_to_pair_list([input_values[index], index + 1])

    get_first_element = lambda item: item[0]
    pair_list.sort(key=get_first_element)

    repeat_list_a = []
    repeat_list_b = []

    for idx in range(input_count):
        value = pair_list[idx][1]
        repeat_list_a += [value] * (value - 1)
        repeat_list_b += [value] * (input_count - value)

    pointer_primary = 0
    pointer_a = 0
    pointer_b = 0
    output_sequence = []
    early_exit_flag = 0

    def get_count_in_output(val):
        return output_sequence.count(val)

    def append_to_output(val):
        output_sequence.append(val)

    for position in range(input_count * input_count):
        did_primary = 0
        if pointer_primary != input_count:
            if position == pair_list[pointer_primary][0] - 1:
                if get_count_in_output(pair_list[pointer_primary][1]) != pair_list[pointer_primary][1] - 1:
                    early_exit_flag = 1
                    break
                append_to_output(pair_list[pointer_primary][1])
                pointer_primary += 1
                did_primary = 1
        if did_primary == 0:
            if pointer_a != len(repeat_list_a):
                append_to_output(repeat_list_a[pointer_a])
                pointer_a += 1
            elif pointer_b != len(repeat_list_b):
                append_to_output(repeat_list_b[pointer_b])
                pointer_b += 1
            else:
                if position != input_count * input_count - 1:
                    early_exit_flag = 1
                    break
    if early_exit_flag == 1:
        print("No")
    else:
        print("Yes")
        print(*output_sequence)

solve()