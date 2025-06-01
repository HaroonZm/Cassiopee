number_of_cases = int(input())

for _ in range(number_of_cases):
    start_value, end_value = map(int, input().split())

    answer_list = []
    if start_value <= 5:
        if start_value > end_value:
            for value in range(start_value, end_value - 1, -1):
                answer_list.append(value)
        else:
            for value in range(start_value, end_value + 1):
                answer_list.append(value)
    elif start_value < end_value:
        for value in range(start_value, end_value + 1):
            answer_list.append(value)
    else:
        for value in range(start_value, 10):
            answer_list.append(value)
        if end_value <= 5:
            for value in range(5, end_value - 1, -1):
                answer_list.append(value)
        else:
            for value in range(5, 0, -1):
                answer_list.append(value)
            for value in range(0, end_value + 1):
                answer_list.append(value)

    print(' '.join(str(number) for number in answer_list))