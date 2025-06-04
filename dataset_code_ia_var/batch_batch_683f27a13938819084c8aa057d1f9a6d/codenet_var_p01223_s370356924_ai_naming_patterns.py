for loop_index in [1] * input():
    list_size = input()
    input_list = map(int, raw_input().split())
    difference_list = [input_list[index + 1] - input_list[index] for index in range(list_size - 1)]
    max_difference = max(0, max(difference_list))
    min_difference = -min(-0, min(difference_list))
    print max_difference, min_difference