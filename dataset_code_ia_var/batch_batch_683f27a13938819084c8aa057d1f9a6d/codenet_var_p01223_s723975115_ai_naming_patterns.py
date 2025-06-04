for test_case_index in range(int(input())):
    sequence_length = int(input())
    sequence_values = list(map(int, input().split()))
    difference_values = [0, 0]
    for element_index in range(1, sequence_length):
        forward_difference = sequence_values[element_index] - sequence_values[element_index - 1]
        backward_difference = sequence_values[element_index - 1] - sequence_values[element_index]
        difference_values = [
            max(forward_difference, difference_values[0]),
            max(backward_difference, difference_values[1])
        ]
    print(difference_values[0], difference_values[1])