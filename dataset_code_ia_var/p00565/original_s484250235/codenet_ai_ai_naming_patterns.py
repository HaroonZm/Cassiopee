input_count = int(input())
input_values = input().split(" ")
sequence_items = [int(input_values[index]) for index in range(input_count)]

maximum_sequence_length = 0
current_sequence_length = 0

for index in range(input_count):
    if sequence_items[index] == 1:
        current_sequence_length += 1
        if maximum_sequence_length < current_sequence_length:
            maximum_sequence_length = current_sequence_length
    else:
        current_sequence_length = 0

print(maximum_sequence_length + 1)