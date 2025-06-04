input_string = input()
step_size = int(input())
result_string = ""
for current_index in range(len(input_string)):
    if current_index % step_size == 0:
        result_string += input_string[current_index]
print(result_string)