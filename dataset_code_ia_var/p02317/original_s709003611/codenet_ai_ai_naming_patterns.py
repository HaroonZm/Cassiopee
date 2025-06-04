import bisect

input_size = int(input())
input_sequence = [0] * input_size
for index_input_sequence in range(input_size):
    input_sequence[index_input_sequence] = int(input())

lis_sequence = [input_sequence[0]]
for index_sequence in range(input_size):
    current_element = input_sequence[index_sequence]
    if current_element > lis_sequence[-1]:
        lis_sequence.append(current_element)
    else:
        position_replace = bisect.bisect_left(lis_sequence, current_element)
        lis_sequence[position_replace] = current_element

print(len(lis_sequence))