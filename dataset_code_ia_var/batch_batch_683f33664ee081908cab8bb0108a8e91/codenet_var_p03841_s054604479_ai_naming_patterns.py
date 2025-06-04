input_count = int(input())
input_values = [int(element) for index, element in enumerate(input().split())]
paired_values = sorted(zip(input_values, range(1, input_count + 1)))

stack_sequence = []
for value, index in paired_values[::-1]:
    for _ in range(index - 1):
        stack_sequence.append(index)

current_position = 1
answer_sequence = []
reserve_sequence = []
used_count = [0] * (input_count + 1)
for idx in range(input_count):
    current_value, current_index = paired_values[idx]
    for _ in range(current_value - current_position):
        if stack_sequence:
            next_element = stack_sequence.pop()
        elif reserve_sequence:
            next_element = reserve_sequence.pop()
        else:
            print('No')
            exit()
        answer_sequence.append(next_element)
        used_count[next_element] += 1
    if used_count[current_index] != current_index - 1:
        print('No')
        exit()
    answer_sequence.append(current_index)
    for _ in range(input_count - current_index):
        reserve_sequence.append(current_index)
    current_position = current_value + 1

answer_sequence += reserve_sequence

print('Yes')
print(*answer_sequence)