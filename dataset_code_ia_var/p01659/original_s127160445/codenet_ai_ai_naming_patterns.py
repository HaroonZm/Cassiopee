input_value = input()
input_sequence = map(int, raw_input().split())
stack_sequence = []
unique_count = 0
for current_element in input_sequence:
    while len(stack_sequence) and stack_sequence[-1] > current_element:
        stack_sequence.pop()
    if (not len(stack_sequence)) or stack_sequence[-1] != current_element:
        unique_count += 1
        stack_sequence.append(current_element)
print unique_count