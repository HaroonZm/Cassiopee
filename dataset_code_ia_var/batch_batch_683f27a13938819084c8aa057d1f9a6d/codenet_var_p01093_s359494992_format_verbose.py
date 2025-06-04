while True:

    number_of_elements = int(input())

    if number_of_elements == 0:
        break

    input_values = list(map(int, input().split()))

    input_values.sort()

    minimum_difference = 1_000_000

    current_difference = 0

    for first_index in range(number_of_elements):
        for second_index in range(first_index + 1, number_of_elements):
            current_difference = abs(input_values[first_index] - input_values[second_index])
            if current_difference <= minimum_difference:
                minimum_difference = current_difference

    print(minimum_difference)