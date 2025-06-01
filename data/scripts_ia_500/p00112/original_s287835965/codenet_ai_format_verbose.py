while True:

    number_of_values = int(input().rstrip())

    if number_of_values == 0:
        break
    else:
        values_list = []

        while number_of_values > 0:
            current_value = int(input())
            values_list.append(current_value)
            number_of_values -= 1

        values_list.sort()

        total_sum = 0
        cumulative_sum = 0

        for value in values_list:
            total_sum += cumulative_sum
            cumulative_sum += value

        print(total_sum)