input_length = int(input())
input_sequence = list(map(int, input().split()))
input_sequence.append(0)
input_sequence.insert(0, 0)
total_difference = 0
for index in range(input_length + 1):
    total_difference += abs(input_sequence[index] - input_sequence[index + 1])
for position in range(1, input_length + 1):
    adjusted_difference = (
        total_difference
        + abs(input_sequence[position - 1] - input_sequence[position + 1])
        - abs(input_sequence[position] - input_sequence[position + 1])
        - abs(input_sequence[position] - input_sequence[position - 1])
    )
    print(adjusted_difference)