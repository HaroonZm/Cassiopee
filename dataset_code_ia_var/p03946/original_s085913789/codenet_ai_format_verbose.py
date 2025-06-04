def main():
    input_num_count, unused_input_value = [int(value) for value in input().split()]

    input_numbers_list = [int(value) for value in input().split()]
    total_numbers = len(input_numbers_list)

    max_difference_list = [0]
    current_minimum = input_numbers_list[0]
    current_trend = 0

    def update_max_difference_list(max_difference_list, new_difference):
        if max_difference_list[0] < new_difference:
            max_difference_list = [new_difference]
        elif max_difference_list[0] == new_difference:
            max_difference_list.append(new_difference)
        return max_difference_list

    previous_number = input_numbers_list[0]

    for current_number in input_numbers_list[1:]:
        if previous_number - current_number > 0:
            if current_trend >= 0:
                max_difference_list = update_max_difference_list(max_difference_list, previous_number - current_minimum)
            current_trend = -1
        elif previous_number - current_number < 0:
            if current_trend <= 0:
                current_minimum = min(previous_number, current_minimum)
            current_trend = 1
        previous_number = current_number

    max_difference_list = update_max_difference_list(max_difference_list, input_numbers_list[-1] - current_minimum)

    print(len(max_difference_list))

main()