def compute_sequence_sum():
    input_length = int(input()) + 1
    input_values = [int(value) for value in input().split()]
    sequence_capacity = [0] * input_length
    for index in range(input_length):
        if index == 0:
            sequence_capacity[index] = 1
        else:
            sequence_capacity[index] = (sequence_capacity[index - 1] - input_values[index - 1]) * 2
        if sequence_capacity[index] <= 0:
            print(-1)
            return
    if sequence_capacity[input_length - 1] < input_values[input_length - 1]:
        print(-1)
        return
    sequence_capacity[input_length - 1] = input_values[input_length - 1]
    total_sum = sequence_capacity[input_length - 1]
    for index in range(input_length - 2, -1, -1):
        sequence_capacity[index] = min(sequence_capacity[index], sequence_capacity[index + 1] + input_values[index])
        if sequence_capacity[index] == 0:
            print(-1)
            return
        total_sum += sequence_capacity[index]
    print(total_sum)

compute_sequence_sum()