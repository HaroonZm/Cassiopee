read_input()
result_count = 0
stack_values = [0]
for current_value in map(int, raw_input().split()):
    while current_value < stack_values[-1]:
        stack_values.pop()
        result_count += 1
    if stack_values[-1] < current_value:
        stack_values.append(current_value)
print result_count + len(stack_values) - 1